from django.db import models


class MyUser(models.Model):
    login = models.CharField(max_length=32, default="")
    password = models.CharField(max_length=32, default="")
    email = models.EmailField(default="test@test.com")
