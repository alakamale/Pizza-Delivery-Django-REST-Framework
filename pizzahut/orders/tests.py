from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Order, Pizza, CustomerAddress
from .views import OrderViewSet, PizzaViewSet, CustomerAddressViewSet, CustomerViewSet

class CustomerTestCase(APITestCase):
     def setUp(self):
         pass
    #     Order.objects(
    #         customer=Customer.objects.get(id=1),
    #         customer_addr=CustomerAddress.objects.get(id=1),
    #         pizza=Pizza.objects.get(id=1),
    #         size="REGULAR",
    #         order_status ="SUBMITTED",
    #     )
    #     self.start_order_count = 1