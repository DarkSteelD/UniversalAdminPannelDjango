from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Business, Product
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортируем необходимый миксин
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class BusinessCreate(LoginRequiredMixin, CreateView):  # Используем LoginRequiredMixin
    model = Business
    fields = ['name', 'address']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.owner = self.request.user  # Установка владельца перед сохранением объекта
        return super().form_valid(form)

class ProductList(LoginRequiredMixin, ListView):  # Используем LoginRequiredMixin
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):  # Если доступ нужен без ограничений, убираем миксин
    model = Product

class ProductCreate(LoginRequiredMixin, CreateView):  # Используем LoginRequiredMixin
    model = Product
    fields = ['name', 'business', 'category', 'supplier', 'price', 'in_stock']
    success_url = reverse_lazy('product-list')

class ProductUpdate(LoginRequiredMixin, UpdateView):  # Используем LoginRequiredMixin
    model = Product
    fields = ['name', 'business', 'category', 'supplier', 'price', 'in_stock']
    success_url = reverse_lazy('product-list')

def index(request):
    return render(request, 'business/index.html', {})

class BusinessDelete(LoginRequiredMixin, DeleteView):  # Используем LoginRequiredMixin
    model = Business
    success_url = reverse_lazy('home')

class ProductDelete(LoginRequiredMixin, DeleteView):  # Используем LoginRequiredMixin
    model = Product
    success_url = reverse_lazy('product-list')
