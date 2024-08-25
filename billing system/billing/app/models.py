from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    product_brand = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name

class Billing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50)

    def __str__(self):
        return f"Billing {self.id} - {self.customer.name}"
