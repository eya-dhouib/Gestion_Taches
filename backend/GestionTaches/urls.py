from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GestionTaches

router = DefaultRouter()
router.register(r'taches', GestionTaches)

urlpatterns = [
    path('', include(router.urls)),
]
