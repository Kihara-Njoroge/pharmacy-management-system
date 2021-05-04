from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Manufacturer)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Invoice)
admin.site.register(Purchase)
