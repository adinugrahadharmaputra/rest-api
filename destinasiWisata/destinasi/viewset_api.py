from destinasi.models import Destinasi,Provinsi
from destinasi.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
        return Response(
                {'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data})
    
    def create(self, request):
        serializer = DestinasiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        destinasi.delete()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data': True
            }
        )

class ProvinsiViewSet(viewsets.ModelViewSet):
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
        return Response(
                {'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data})
    
    def create(self, request):
        serializer = DestinasiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        destinasi.delete()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data': True
            }
        )
    # permission_classes = [permissions.IsAuthenticated]
