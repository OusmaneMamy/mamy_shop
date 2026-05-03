from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitViewSet

router = DefaultRouter()
router.register('produits', ProduitViewSet, basename="produits")

urlpatterns = [
    path('', include(router.urls)),
]