from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-customer/', views.add_customer,name='add_customer'),
    path('view-customers/', views.view_customers,name='view_customers'),
    path('add-inventory/', views.add_inventory,name='add_inventory'),
    path('billing/', views.billing,name='billing'),
    path('view-billing/', views.view_billing,name='view_billing'),
]
