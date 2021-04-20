from destinasi.models import Provinsi
from destinasi.serializers import PovinsiSerializer
from rest_framework import viewsets, permissions

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = PovinsiSerializer
    permission_classes = [permissions.IsAuthenticated]