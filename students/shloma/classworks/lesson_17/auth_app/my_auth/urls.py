from django.urls import path
from .views import index, login, logout, registration, main


urlpatterns = [
    path('', index, name="index"),
    path('registration/', registration, name="registration"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('main/', main, name="main"),
]
