import django_filters
from django_filters import CharFilter, NumberFilter, DateFilter
from .models import *


class CustomerFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name',
                            lookup_expr='icontains', label='First Name')
    second_name = CharFilter(field_name='second_name',
                             lookup_expr='icontains', label='Second Name')

    class Meta:
        model = Customer
        fields = ['first_name', 'second_name']


class SupplierFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')

    class Meta:
        model = Supplier
        fields = ['name']


class ManufacturerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')

    class Meta:
        model = Supplier
        fields = ['name']


class MedicineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    generic_name = CharFilter(
        field_name='generic_name', lookup_expr='icontains', label='Generic Name')

    class Meta:
        model = Medicine
        fields = ['name', 'generic_name']


class PurchaseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_of_purchase',
                            lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name='date_of_purchase',
                          lookup_expr='lte', label='End Date')

    class Meta:
        model = Purchase
        fields = ['status']


class InvoiceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created',
                            lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name='date_created',
                          lookup_expr='lte', label='End Date')

    class Meta:
        model = Invoice
        fields = ['customer', 'status', ]
