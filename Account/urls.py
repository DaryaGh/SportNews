from django.urls import path
from .views import auth_logout ,auth_login,auth_register

urlpatterns = [
    # path('Register/', register, name='register'),
    path('register', auth_register , name='auth_register'),
    path('login', auth_login , name='auth_login'),
    path('logout', auth_logout , name='auth_logout'),
]