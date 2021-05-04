from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    total_customers = customers.count()

    medicine = Medicine.objects.all()
    total_medicine = medicine.count()

    context = {'total_customers': total_customers,
               'total_medicine': total_medicine}
    return render(request, 'index.html', context)


# Customers
def customerList(request):
    customers = Customer.objects.all()

    paginator = Paginator(customers, 10)
    page_number = request.GET.get('page', 1)
    customer_obj = paginator.get_page(page_number)
    context = {'customers': customers, 'customer_obj': customer_obj}
    return render(request, 'customers\customer_list.html', context)


def addCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {"form": form}
    return render(request, 'customers\customer_add.html', context)


def creditCustomers(request):
    customers = Customer.objects.all().filter(payment='credit')
    context = {'customers': customers}
    return render(request, 'customers\credit_customers.html', context)


# Suppliers
def suppliersList(request):
    suppliers = Supplier.objects.all()
    paginator = Paginator(suppliers, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'suppliers': suppliers, 'page_obj': page_obj}
    return render(request, 'suppliers\suppliers_list.html', context)


def addSupplier(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    context = {'form': form}
    return render(request, 'suppliers\supplier_add.html', context)


# Manufacturer
def manufacturersList(request):
    manufacturers = Manufacturer.objects.all()
    paginator = Paginator(manufacturers, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'manufacturers': manufacturers, 'page_obj': page_obj}
    return render(request, 'manufacturers\manufacturers_list.html', context)


def addManufacturer(request):
    form = ManufacturerForm
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturers')
    context = {'form': form}
    return render(request, 'manufacturers\manufacturer_add.html', context)


def medicineList(request):
    medicines = Medicine.objects.all()
    paginator = Paginator(medicines, 7)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'medicines': medicines, 'page_obj': page_obj}
    return render(request, 'medicines\medicine_list.html', context)


def addMedicine(request):
    form = MedicineForm()
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine')
    context = {'form': form}
    return render(request, 'medicines\medicine_add.html', context)


# Invoice
def invoiceList(request):
    invoices = Invoice.objects.all()
    paginator = Paginator(invoices, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'invoices': invoices, 'page_obj': page_obj}
    return render(request, 'invoices\invoices_list.html', context)


def addInvoice(request):
    form = InvoiceForm()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoices')
    context = {'form': form}
    return render(request, 'invoices\invoice_add.html', context)


# Purschases
def purchaseList(request):
    purchases = Purchase.objects.all()
    paginator = Paginator(purchases, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {'purchases': purchases, 'page_obj': page_obj}

    return render(request, 'purchases\purchases_list.html', context)


def addPurchase(request):
    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    context = {'form': form}

    return render(request, 'purchases\purchase_add.html', context)
