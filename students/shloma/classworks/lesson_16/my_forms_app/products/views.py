from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products
from .forms import ProductsForm, ProductModelForm


def products(request):
    goods = Products.objects.all()

    if request.method == "GET":

        data = [] # Список всех форм для всех продуктов

        for good in goods:
            form = ProductModelForm(prefix=str(good.pk), initial={"current_amont": good.current_amont})
            data.append({"good": good, "form": form})

        return render(request, "products/goods.html", context={"data": data})

    elif request.method == "POST":

        # form = ProductModelForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
        #     p = Products(**form.cleaned_data)
        #     p.save()
        #     print(p)
        # else:
        #     return HttpResponse("Invalid data")

        for good in goods:
            form = ProductModelForm(request.POST, prefix=str(good.pk))

            if form and form.is_valid():
                good.current_amont = form.cleaned_data.get("current_amont", good.current_amont)
                good.save()
                print("Saved")
            else:
                print(f"Form '{form}' invalid")

        return redirect("products")


