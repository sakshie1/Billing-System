from django.contrib import admin
from .models import Customer, Inventory, Billing

admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Billing)
