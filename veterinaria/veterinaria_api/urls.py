from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'duenos', PropietarioViewSet)
router.register(r'mascotas', PacienteViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'desparacitaciones', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
