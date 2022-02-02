from django.db import models


# Create your models here.

class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __repr__(self):
        return f"id='{self.id}', Author: '{self.name}', city: '{self.city}'"

    def __str__(self):
        return f"id='{self.id}', Author: '{self.name}', city: '{self.city}'"


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __repr__(self):
        return f"id='{self.id}', Title: '{self.name}', author_id='{self.author_id}'"

    def __str__(self):
        return f"id='{self.id}', Title: '{self.name}', author_id='{self.author_id}'"
