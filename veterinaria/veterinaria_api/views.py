from rest_framework import viewsets
from .models import Propietario
from .serializers import PropietarioSerializer


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
