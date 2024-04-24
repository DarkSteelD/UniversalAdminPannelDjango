from django.contrib import admin
from .models import Business, Category, Supplier, Product, Service
from django.contrib.admin import DateFieldListFilter, RelatedOnlyFieldListFilter

class ProductInline(admin.TabularInline):  
    model = Product
    extra = 1

class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'address']
    search_fields = ['name', 'owner__username']
    inlines = [ProductInline]  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info']
    list_filter = ['name']  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'business', 'category', 'price', 'in_stock')
    list_filter = ('category', 'in_stock', 'business__owner')  
    search_fields = ('name',)
    list_editable = ('price', 'in_stock')  

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'business', 'price']
    list_filter = ['business', 'price']  
    search_fields = ['name']

admin.site.register(Business, BusinessAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
