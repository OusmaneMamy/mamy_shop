from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitVariationViewSet

router = DefaultRouter()


router.register('produitvariations', ProduitVariationViewSet, basename='produitvariations')

urlpatterns = [
    path('', include(router.urls)),
]