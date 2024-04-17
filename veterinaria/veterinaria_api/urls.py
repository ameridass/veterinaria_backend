from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet, PacienteViewSet, CitaViewSet

router = DefaultRouter()
router.register(r'duenos', PropietarioViewSet)
router.register(r'mascotas', PacienteViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
