import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybusiness.settings')
django.setup()

from django.contrib.auth.models import User
from business.models import Business, Category, Supplier, Product, Service

def create_data():
    # Создание пользователей
    for i in range(10):
        user = User.objects.create_user(f'username{i}', f'email{i}@example.com', 'password')

        # Бизнес
        business = Business.objects.create(owner=user, name=f"Sample Business {i}", address=f"{i} Business Ave")

        # Категории
        category = Category.objects.create(name=f"Category {i}")

        # Поставщики
        supplier = Supplier.objects.create(name=f"Global Supplies {i}", contact_info=f"Contact Info {i}")

        # Продукты
        product = Product.objects.create(
            business=business,
            name=f"Sample Product {i}",
            category=category,
            supplier=supplier,
            price=random.uniform(100.0, 500.0),  # Случайная цена
            in_stock=bool(random.getrandbits(1))  # Случайное наличие на складе
        )

        # Услуги
        service = Service.objects.create(
            business=business,
            name=f"Consulting {i}",
            price=random.uniform(200.0, 600.0)  # Случайная цена
        )

if __name__ == '__main__':
    create_data()
