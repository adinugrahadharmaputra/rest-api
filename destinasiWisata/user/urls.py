from .viewset_api import LoginAPI,ProfileViewSet
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('profile/', ProfileViewSet.as_view() , name='profile'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]