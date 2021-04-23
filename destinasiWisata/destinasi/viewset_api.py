from destinasi.models import Destinasi,Provinsi
from destinasi.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

## Destinasi
class DestinasiViewSet(viewsets.ModelViewSet):
    serializer_class = DestinasiSerializer

    # GET Destinasi
    def list(self, request):
        queryset = Destinasi.objects.all()
        serializer = DestinasiSerializer(queryset, many=True)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )

    # GET Detail Destinasi
    def retrieve(self, request, pk=None):
        queryset = Destinasi.objects.all()
        destinasi = get_object_or_404(queryset, pk=pk)
        serializer = DestinasiSerializer(destinasi)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )

    # Post Destinasi
    def create(self, request, format=None):
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

    # PUT Destinasi
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

    # PATCH Destinasi
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
    
    # DELETE Destinasi
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



## Provinsi
class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer

    # GET Provinsi
    def list(self, request):
        queryset = Provinsi.objects.all()
        serializer = ProvinsiSerializer(queryset, many=True)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )

    # GET Detail Provinsi
    def retrieve(self, request, pk=None):
        queryset = Provinsi.objects.all()
        provinsi = get_object_or_404(queryset, pk=pk)
        serializer = ProvinsiSerializer(provinsi)
        return Response(
            {
               'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )
    
    # POST Provinsi
    def create(self, request):
        serializer = ProvinsiSerializer(data=request.data)
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

    # PUT Provinsi
    def update(self, request, pk=None):
        queryset = Provinsi.objects.all()
        provinsi = get_object_or_404(queryset, pk=pk)
        serializer = ProvinsiSerializer(provinsi, data=request.data)
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

    # PATCH Provinsi
    def partial_update(self, request, pk=None):
        queryset = Provinsi.objects.all()
        provinsi = get_object_or_404(queryset, pk=pk)
        serializer = ProvinsiSerializer(provinsi, data=request.data)
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

    # DELETE Provinsi
    def destroy(self, request, pk=None):
        queryset = Provinsi.objects.all()
        provinsi = get_object_or_404(queryset, pk=pk)
        provinsi.delete()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data': True
            }
        )
