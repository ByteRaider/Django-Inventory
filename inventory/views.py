from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import csv
from .models import Product, Category, Transaction
from .forms import SignUpForm, ProductForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'inventory/product_list.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.select_related('category').filter(Q(name__icontains=query) | Q(category__name__icontains=query))
        return Product.objects.select_related('category').all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            if product.stock <= 5:
                product.color = 'danger'
            elif product.stock > 5 and product.stock <= 10:
                product.color = 'warning'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Category', 'Price', 'Stock'])

    for product in Product.objects.all():
        writer.writerow([product.name, product.category.name, product.price, product.stock])

    return response



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to a 'success' page or the inventory index
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
