from django.urls import path
from .views import registration, login, logout, main

urlpatterns = [
    path('registration/', registration),
    path('login/', login, name="login"),
    path('logout/', logout),
    path('main/', main),
]
