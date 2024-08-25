from django.shortcuts import render, redirect
from .models import Customer, Inventory, Billing
from .forms import CustomerForm, InventoryForm, BillingForm

def dashboard(request):
    customer_count = Customer.objects.count()
    inventory_count = Inventory.objects.count()
    billing_count = Billing.objects.count()
    return render(request, 'dashboard.html', {
        'customer_count': customer_count,
        'inventory_count': inventory_count,
        'billing_count': billing_count
    })

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'view_customers.html', {'customers': customers})

def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InventoryForm()
    return render(request, 'add_inventory.html', {'form': form})

def billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = form.save(commit=False)
            billing.total_price = billing.product.product_price * billing.total_quantity
            billing.save()
            return redirect('dashboard')
    else:
        form = BillingForm()
    return render(request, 'billing.html', {'form': form})

def view_billing(request):
    billings = Billing.objects.all()
    return render(request, 'view_billing.html', {'billings': billings})
