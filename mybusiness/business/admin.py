from django.contrib import admin
from .models import Business, Category, Supplier, Product, Service

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'address']
    search_fields = ['name', 'owner__username']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'category', 'price', 'in_stock')
    list_filter = ('category', 'in_stock', 'business')
    search_fields = ('name',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'business', 'price']
    list_filter = ['business']
    search_fields = ['name']

admin.site.register(Business, BusinessAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
