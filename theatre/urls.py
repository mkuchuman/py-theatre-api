from django.urls import path, include
from rest_framework.routers import DefaultRouter

from theatre.views import GenreViewSet, ActorViewSet, TheatreHallViewSet, PlayViewSet, PerformanceViewSet

app_name = "theatre"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)

urlpatterns = [
    path("", include(router.urls))
]
