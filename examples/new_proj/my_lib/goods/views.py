from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def get_products(request):
    data = serializers.serialize('json', Products.objects.all(), fields=("name", "current_amount"))
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def set_current_amount_products(request):
    products_list = json.loads(request.body)["rows"]
    # [{'name': 'молоко', 'current_amount': 2}, {'name': 'coffee', 'current_amount': 1}]
    for pr in products_list:
        for i in Products.objects.all().filter(name=pr["name"]):
            i.current_amount = pr["current_amount"]
            i.save()

    return HttpResponse("OK")
