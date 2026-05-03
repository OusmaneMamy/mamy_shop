from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CouleurViewSet

router = DefaultRouter()
router.register('couleurs', CouleurViewSet, basename='couleurs')

urlpatterns = [
    path('', include(router.urls)),
]