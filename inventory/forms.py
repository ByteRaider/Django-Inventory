from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'stock', 'description', 'category' )
        sortable_fields = ('name', 'price', 'stock', 'category' )
