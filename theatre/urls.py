from rest_framework.routers import DefaultRouter

from theatre.views import GenreViewSet, ActorViewSet, TheatreHallViewSet, PlayViewSet, PerformanceViewSet, \
    ReservationViewSet

app_name = "theatre"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_halls", TheatreHallViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = router.urls
