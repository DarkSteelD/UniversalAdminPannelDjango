from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup
urlpatterns = [
    path('', views.index, name='home'),
    path('business/add/', views.BusinessCreate.as_view(), name='business-add'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/add/', views.ProductCreate.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product-update'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('business/<int:pk>/delete/', views.BusinessDelete.as_view(), name='business-delete'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('signup/', signup, name='signup'),
]

