from django.urls import path, include
from rest_framework.routers import DefaultRouter

from theatre.views import GenreViewSet, ActorViewSet

app_name = "theatre"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
