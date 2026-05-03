from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TailleViewSet

router = DefaultRouter()
router.register('tailles', TailleViewSet, basename='tailles')


urlpatterns = [
    path('', include(router.urls)),
]