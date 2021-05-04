from django.forms import ModelForm
from django import forms
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = ['invoice_no', 'invoice_id']


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        exclude = ['purchase_no', 'purchase_id']
