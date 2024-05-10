from theatre.models import Genre, Actor, TheatreHall, Play, Performance
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name",)


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description", "actors", "genres")


class PlayListSerializer(PlaySerializer):
    actors = serializers.SlugRelatedField(many=True, read_only=True, slug_field="full_name")
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")


class PlayDetailSerializer(PlaySerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", "play", "theatre_hall", "show_time")


class PerformanceListSerializer(PerformanceSerializer):
    play_title = serializers.CharField(source="play.title", read_only=True)
    theatre_hall_name = serializers.CharField(source="theatre_hall.name", read_only=True)
    theatre_hall_capacity = serializers.IntegerField(source="theatre_hall.capacity")

    class Meta:
        model = Performance
        fields = ("id",
                  "play_title",
                  "theatre_hall_name",
                  "theatre_hall_capacity",
                  "show_time",
                  "tickets_available",
                  )


class PerformanceDetailSerializer(PerformanceSerializer):
    play = PlaySerializer(many=False, read_only=True)
    theatre_hall = TheatreHallSerializer(many=False, read_only=True)

    class Meta:
        model = Performance
        field = ("id",
                 "play",
                 "theatre_hall",
                 "show_time",
                 )
