from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('customer_list/', customerList, name='customers'),
    path("add_customer/", addCustomer, name='add_customer'),
    path("credit-customers/", creditCustomers, name='credit_customers'),

    path('supplier_list/', suppliersList, name='suppliers'),
    path('add_supllier', addSupplier, name='add_supplier'),

    path('manufacturer_list/', manufacturersList, name='manufacturer'),
    path('add_manufacturer', addManufacturer, name='add_manufacturer'),

    path('medicine_list/', medicineList, name='medicine'),
    path('add_medicine/', addMedicine, name='add_medicine'),

    path('invoice_list/', invoiceList, name='invoices'),
    path('add_invoice/', addInvoice, name='add_invoice'),

    path('purchases_list/', purchaseList, name='purchase_list'),
    path('purchase_add/', addPurchase, name='add_purchase')
]
