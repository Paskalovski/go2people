from django.shortcuts import render
from . import models
from django.views.generic import (TemplateView, ListView, DetailView)



class ProductListView(ListView):
    context_object_name = 'products'
    model = models.Product


class ProductDetailView(DetailView):
    context_object_name = "product_detail"
    model = models.Product
