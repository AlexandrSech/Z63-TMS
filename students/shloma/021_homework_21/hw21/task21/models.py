from django.db import models
from django.urls import reverse


# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50,
                                 help_text="Введите имя",
                                 verbose_name="Имя",
                                 null=False)

    lastname = models.CharField(max_length=50,
                                help_text="Введите фамилию",
                                verbose_name="Фамилия",
                                null=False)

    age = models.IntegerField(null=False,
                              help_text="Введите возраст",
                              verbose_name="Возраст")

    profession = models.CharField(max_length=100,
                                  help_text="Введите профессию",
                                  verbose_name="Профессия",
                                  default="No info")

    def __repr__(self):
        return f"id={self.id}: {self.firstname} {self.lastname}"

    def __str__(self):
        return self.__repr__()

    def get_url(self):
        return reverse("person_detail", args=[self.id])
