from .viewset_api import LoginAPI,LogoutAPI
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    
    path('login/', LoginAPI.as_view(), name='login'),
    path('user/logout/', LogoutAPI.as_view(), name='logout'),
   ]