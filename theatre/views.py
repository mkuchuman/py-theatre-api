from django.shortcuts import render
from rest_framework import viewsets, permissions

from theatre.models import Genre, Actor
from theatre.serializers import GenreSerializer, ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = ()


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # permission_classes = ()
