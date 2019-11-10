from rest_framework import routers
from .views import OrderViewSet, CustomerViewSet, PizzaViewSet, CustomerAddressViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register('customers/(?P<customer_id>\d+)/orders', OrderViewSet, base_name='customer_orders')
router.register('customers/(?P<customer_id>\d+)/addresses', CustomerAddressViewSet, base_name='customer_addresses')
router.register('customers', CustomerViewSet, base_name='customers')
router.register('pizzas', PizzaViewSet, base_name='pizzas')

urlpatterns = [
    path('', include(router.urls)),
]