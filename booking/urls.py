from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import BookingViewSet
from .views import BookingViewSet, MenuItemViewSet


router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'menu-items', MenuItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
     path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
