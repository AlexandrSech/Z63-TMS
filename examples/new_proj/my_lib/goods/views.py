from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .forms import ProductsForm


def get_products(request):
    # data = serializers.serialize('json', Products.objects.all(), fields=("name", "current_amount"))
    # return HttpResponse(data, content_type="application/json")
    data = Products.objects.all()


    template = loader.get_template('goods/get_products.html')

    template_dict = {'id': data[0].id, 'name': data[0].name, "current_amount": data[0].current_amount}

    print(template_dict)


    return HttpResponse(template.render(template_dict, request))
    # render(request, template, {'name': data[0].name, 'amount': data[0].current_amount})




@csrf_exempt
def set_current_amount_products(request):
    form = ProductsForm(request.POST)


    print(form.data)


    """products_list = json.loads(request.body)["rows"]
    # [{'name': 'молоко', 'current_amount': 2}, {'name': 'coffee', 'current_amount': 1}]
    for pr in products_list:
        for i in Products.objects.all().filter(name=pr["name"]):
            i.current_amount = pr["current_amount"]
            i.save()"""

    return HttpResponse("OK")
