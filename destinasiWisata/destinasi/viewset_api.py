from destinasi.models import Destinasi,Provinsi
from destinasi.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response

class DestinasiViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Destinasi.objects.all()
        serializer = DestinasiSerializer(queryset, many=True)
        return Response({
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            })

    def retrieve(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi)
        return Response(serializer.data)
    # permission_classes = [permissions.IsAuthenticated]

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer
    # permission_classes = [permissions.IsAuthenticated]