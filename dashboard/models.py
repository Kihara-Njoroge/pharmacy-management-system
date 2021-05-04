from django.db import models
import uuid


class Customer(models.Model):
    gender_choice = (
        ('male', 'male',),
        ('female', 'female'),
        ('other', 'other')
    )
    payment_choice = (
        ('cash', 'cash'),
        ('credit', 'credit')
    )

    first_name = models.CharField(max_length=254)
    second_name = models.CharField(max_length=254)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=254, choices=gender_choice)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    phone = models.IntegerField()
    county = models.CharField(max_length=254)
    town = models.CharField(max_length=254)
    payment = models.CharField(
        max_length=254, choices=payment_choice)
    balance = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.first_name

    @property
    def get_name(self):
        full_name = self.first_name + ' ' + self.second_name

        return full_name


class Manufacturer(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    phone = models.IntegerField()
    county = models.CharField(max_length=254)
    town = models.CharField(max_length=254)
    balance = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    phone = models.IntegerField()
    county = models.CharField(max_length=254)
    town = models.CharField(max_length=254)
    balance = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    category_choices = (
        ('liquid', 'liquid'),
        ('tablet', 'tablet'),
        ('capsules', 'capsules'),
        ('inhaler', 'inhalers'),
        ('injections', 'injections'),
        ('implants\\patches', 'implants\\patches'),
        ('ointment\\creams', 'ointment\\creams'),
        ('spray', 'spray'),
        ('drops', 'drops')
    )
    name = models.CharField(max_length=254)
    generic_name = models.CharField(max_length=254)
    category = models.CharField(max_length=254, choices=category_choices)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=254)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    manufacturer_price = models.DecimalField(decimal_places=2, max_digits=7)
    strength = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Invoice(models.Model):
    payment_choices = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('Mpesa', 'Mpesa'),
    )
    status_options = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateField(auto_created=True, null=True)
    invoice_no = models.AutoField(primary_key=True)
    invoice_id = models.UUIDField(default=uuid.uuid4, editable=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    exipry_date = models.DateField(auto_now=False)
    quantity = models.IntegerField()
    box_quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    VAT = models.DecimalField(decimal_places=2, max_digits=10)
    Total = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=254, choices=payment_choices)
    status = models.CharField(max_length=254, choices=status_options)


class Purchase(models.Model):
    payment_choices = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('Mpesa', 'Mpesa'),
    )
    status_options = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    )

    manufacturer = models.ForeignKey(
        Manufacturer, blank=True, null=True, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Supplier, blank=True, null=True,  on_delete=models.CASCADE)
    date_of_purchase = models.DateField(auto_created=True, null=True)
    purchase_no = models.AutoField(primary_key=True)
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    box_quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    VAT = models.DecimalField(decimal_places=2, max_digits=10)
    Total = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=254, choices=payment_choices)
    status = models.CharField(max_length=254, choices=status_options)

    def __str__(self):
        return str(self.purchase_id)

    @property
    def get_name(self):
        if self.manufacturer:
            return self.manufacturer
        else:
            return self.supplier
