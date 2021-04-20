from destinasi.models import Destinasi
from destinasi.serializers import DestinasiSerializer
from rest_framework import viewsets, permissions

class DestinasiViewSet(viewsets.ModelViewSet):
    queryset = Destinasi.objects.all()
    serializer_class = DestinasiSerializer
    permission_classes = [permissions.IsAuthenticated]