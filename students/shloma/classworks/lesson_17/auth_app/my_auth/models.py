from django.db import models


# Create your models here.
class MyUser(models.Model):
    login = models.CharField(max_length=50, verbose_name="Login", null=True)
    password = models.CharField(max_length=50, verbose_name="Password", null=True)
    email = models.EmailField(max_length=50, verbose_name="E-mail", null=True)

    def __str__(self):
        return f"User: {self.login} (e-mail: {self.email})"