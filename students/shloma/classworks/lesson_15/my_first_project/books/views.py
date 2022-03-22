from django.http import HttpResponse
from rest_framework import viewsets

from .models import Books
from .serializers import SimpleBooksSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = SimpleBooksSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the books index.")
