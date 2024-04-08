from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet

router = DefaultRouter()
router.register(r'duenos', PropietarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
