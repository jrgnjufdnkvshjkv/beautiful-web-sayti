from django.shortcuts import render
from .models import Odam, Product,Car,Oila
# Create your views here.


def odamlistview(request):
    odamlar = Odam.objects.all()
    context = {
        "odamlar": odamlar,
    }
    return render(request, "odam.html", context=context)

def productlistview(request):
    productlar = Product.objects.all()
    context = {
        "productlar": productlar,
    }
    return render(request, "product.html", context=context)


def carlistview(request):
    cars = Car.objects.all()
    context = {
        "cars": cars,
    }
    return render(request, "car.html", context=context)


def oilalistview(request):
    oilalar = Oila.objects.all()
    context = {
        "oilalar": oilalar,
    }
    return render(request, "oila.html", context=context)