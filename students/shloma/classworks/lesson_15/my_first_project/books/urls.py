from django.urls import path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('books/', include(router.urls)),
]
