from django import forms
from .models import Customer, Inventory, Billing

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'contact', 'state', 'city']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'product_price', 'product_quantity', 'product_brand', 'supplier_name']

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['customer', 'product', 'total_quantity', 'payment_mode']
