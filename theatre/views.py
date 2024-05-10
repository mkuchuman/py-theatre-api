from django.shortcuts import render
from rest_framework import viewsets, permissions

from theatre.models import Genre, Actor, TheatreHall
from theatre.serializers import GenreSerializer, ActorSerializer, TheatreHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = ()


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # permission_classes = ()


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    # permission_classes = ()