from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('business/add/', views.BusinessCreate.as_view(), name='business-add'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/add/', views.ProductCreate.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product-update'),
]
