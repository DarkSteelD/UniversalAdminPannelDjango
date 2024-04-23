from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Business, Product
from django.shortcuts import render
class BusinessCreate(CreateView):
    model = Business
    fields = ['name', 'address']
    success_url = reverse_lazy('home')

class ProductList(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'business', 'category', 'supplier', 'price', 'in_stock']
    success_url = reverse_lazy('product-list')

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'business', 'category', 'supplier', 'price', 'in_stock']
    success_url = reverse_lazy('product-list')

def index(request):
    return render(request, 'business/index.html', {})
