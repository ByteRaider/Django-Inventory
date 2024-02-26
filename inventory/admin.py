from django.contrib import admin
from .models import Category, Product, Transaction
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'transaction_type', 'created_at')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)