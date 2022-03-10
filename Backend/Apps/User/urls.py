from django.urls import path

from .views import GetName, RegisterUser

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('get_name', GetName.as_view(), name='get_name'),
    path('register/', RegisterUser.as_view(), name='register')
]