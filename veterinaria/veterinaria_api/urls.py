from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet, PacienteViewSet

router = DefaultRouter()
router.register(r'duenos', PropietarioViewSet)
router.register(r'mascotas', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls))
]
