from django.urls import path, include
from rest_framework.routers import DefaultRouter

from theatre.views import GenreViewSet, ActorViewSet, TheatreHallViewSet

app_name = "theatre"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)

urlpatterns = [
    path("", include(router.urls))
]
