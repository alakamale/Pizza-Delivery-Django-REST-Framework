from django.contrib import admin
from .models import Pizza, Order, Customer

# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Pizza)