from rest_framework import generics, viewsets
from .models import Order, Customer, Pizza, CustomerAddress
from .serializers import OrderSerializer, CustomerSerializer, PizzaSerializer, CustomerAddressSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAddressSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return CustomerAddress.objects.filter(customer_id=customer_id)


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.filter()
    serializer_class = PizzaSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer_id=customer_id)
