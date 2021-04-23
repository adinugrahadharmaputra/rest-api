from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework import viewsets, status
from user.models import *
from django.shortcuts import get_object_or_404

## Register API
class RegisterViewSet(viewsets.ViewSet):
    serializer_class = RegisterSerializer
    # GET Register
    def create(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success',
                    'data' : serializer.data
                }
            )
        else:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'bad request',
                    'data' : serializer._errors
                }
            )


## Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    # GET Login
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


## Logout API
class LogoutAPI(KnoxLogoutView):
    permission_classes = [permissions.IsAuthenticated]
    # POST Logout
    def post(self, request, format=None):
        request._auth.delete()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success'
            }
        )

## Profile
class ProfileViewSet(viewsets.ViewSet):
    # GET Profile
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )

    permission_classes = [permissions.IsAuthenticated]
    #GET Profile Detail
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success',
                'data' : serializer.data
            }
        )

        permission_classes = [permissions.IsAuthenticated]
    