from destinasi.models import Destinasi,Provinsi
from destinasi.serializers import DestinasiSerializer,ProvinsiSerializer
from rest_framework import viewsets, permissions

class DestinasiViewSet(viewsets.ModelViewSet):
    queryset = Destinasi.objects.all()
    serializer_class = DestinasiSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer
    # permission_classes = [permissions.IsAuthenticated]