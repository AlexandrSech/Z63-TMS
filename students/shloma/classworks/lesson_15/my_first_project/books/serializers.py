from rest_framework import serializers
from .models import Books, Authors


class SimpleBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            "id",
            "name",
            "author_id",
        )


class SimpleAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = (
            "id",
            "name",
            "city",
        )
