from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, signup, pos_view


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('pos/', pos_view, name='pos'),
]