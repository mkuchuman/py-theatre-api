from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from theatre.models import Play, TheatreHall, Performance, Ticket, Reservation


class ModelTests(TestCase):

    def test_play_string_representation(self):
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        self.assertEqual(str(play), "Hamlet")

    def test_theatre_hall_capacity(self):
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        self.assertEqual(hall.capacity, 200)

    def test_ticket_validation_fail(self):
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        performance = Performance.objects.create(
            play=play, theatre_hall=hall, show_time="2022-06-02 14:00:00"
        )
        ticket = Ticket(row=15, seat=25, performance=performance)
        with self.assertRaises(ValidationError):
            ticket.clean()


class ViewSetTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="user@email.com", password="testpass"
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_play_list_unauthenticated(self):
        self.client.logout()
        url = reverse("theatre:play-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_play_list_authenticated(self):
        url = reverse("theatre:play-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_performance_as_admin(self):
        admin = get_user_model().objects.create_superuser(
            email="admin@example.com", password="adminpass"
        )
        self.client.force_authenticate(user=admin)
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        url = reverse("theatre:performance-list")
        data = {
            "play": play.id,
            "theatre_hall": hall.id,
            "show_time": "2023-01-01T10:00:00Z",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reservation_and_ticket_creation(self):
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        performance = Performance.objects.create(
            play=play, theatre_hall=hall, show_time="2023-01-01T10:00:00Z"
        )
        url = reverse("theatre:reservation-list")
        data = {
            "tickets": [
                {"row": 10, "seat": 20, "performance": performance.id},
                {"row": 5, "seat": 10, "performance": performance.id},
            ]
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        reservation_id = response.data["id"]
        reservation = Reservation.objects.get(id=reservation_id)
        self.assertEqual(reservation.tickets.count(), 2)
        self.assertTrue(
            Ticket.objects.filter(reservation=reservation, row=10, seat=20).exists()
        )
        self.assertTrue(
            Ticket.objects.filter(reservation=reservation, row=5, seat=10).exists()
        )

    def test_ticket_creation_validation(self):
        play = Play.objects.create(title="Hamlet", description="A Shakespeare play")
        hall = TheatreHall.objects.create(name="Main", rows=10, seats_in_row=20)
        performance = Performance.objects.create(
            play=play, theatre_hall=hall, show_time="2023-01-01T10:00:00Z"
        )
        url = reverse("theatre:reservation-list")
        data = {"tickets": [{"row": 11, "seat": 21, "performance": performance.id}]}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
