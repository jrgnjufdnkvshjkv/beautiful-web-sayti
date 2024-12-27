from .views import odamlistview
from .views import productlistview
from .views import carlistview
from .views import oilalistview
from django.urls import path

urlpatterns= [
    path("odamlar", odamlistview, name="odamlar"),
    path("product", productlistview, name="product"),
    path("car", carlistview, name="car"),
    path("oila", oilalistview, name="oila")
]








