from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VenteViewSet

router = DefaultRouter()
router.register(r'ventes', VenteViewSet, basename='ventes')

urlpatterns = [
    path('', include(router.urls)),
]
