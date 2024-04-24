from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Business, Product
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортируем необходимый миксин
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def index(request):
    user_businesses = Business.objects.filter(owner=request.user)
    businesses_with_products = {
        business: Product.objects.filter(business=business) for business in user_businesses
    }
    context = {
        'businesses_with_products': businesses_with_products
    }
    return render(request, 'business/index.html', context)

class BusinessCreate(LoginRequiredMixin, CreateView):  # Используем LoginRequiredMixin
    model = Business
    fields = ['name', 'address']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.owner = self.request.user  # Установка владельца перед сохранением объекта
        return super().form_valid(form)


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'  # Убедитесь, что у вас правильно указан путь к шаблону
    paginate_by = 10  # Количество элементов на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context


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

class BusinessList(ListView):
    model = Business
    context_object_name = 'businesses'
    template_name = 'business/business_list.html'  # Убедитесь, что у вас правильно указан путь к шаблону
    paginate_by = 10  # Количество бизнесов на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')

        try:
            businesses = paginator.page(page)
        except PageNotAnInteger:
            businesses = paginator.page(1)
        except EmptyPage:
            businesses = paginator.page(paginator.num_pages)

        context['businesses'] = businesses
        return context