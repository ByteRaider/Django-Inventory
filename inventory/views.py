from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import csv
from .models import Product, Category, Transaction

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory/product_list.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return super().get_queryset()

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')
    template_name = 'inventory/product_confirm_delete.html'

def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Price', 'Stock'])

    for product in Product.objects.all():
        writer.writerow([product.name, product.category.name, product.price, product.stock])

    return response
