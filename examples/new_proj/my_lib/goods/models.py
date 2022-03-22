from django.db import models


class ClientProducts(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    value = models.IntegerField()


class Suppliers(models.Model):
    name = models.CharField(max_length=200)
    payment_deferment = models.IntegerField()   # количество календарных дней отсрочки платежа
    is_active = models.BooleanField()


class Products(models.Model):
    name = models.CharField(max_length=200)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    current_amount = models.IntegerField()
    update_date = models.DateTimeField(auto_now_add=True)


class Supplies(models.Model):
    supplier = models.ForeignKey(Suppliers, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    delivery_amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_paid = models.BooleanField()
