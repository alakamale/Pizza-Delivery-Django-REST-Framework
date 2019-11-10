from django.db import models

# Create your models here.
STATUS_ORDER_CHOICES = (
    ('SUBMITTED', 'Submitted'),
    ('PRODUCTION', 'In Production'),
    ('DELIVERING', 'Left to Deliver'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
)

PIZZA_SIZES = (
    ('REGULAR', 'Regular'),
    ('MEDIUM', 'Medium'),
    ('LARGE', 'Large'),
)

class Customer(models.Model):
    db_table = 'customer'

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.first_name+" "+ self.last_name

class CustomerAddress(models.Model):
    db_table = 'customer_address'

    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    address = models.TextField(null=False)

    def __str__(self):
        return self.address


class Pizza(models.Model):
    db_table = 'pizza'

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    db_table = 'order'

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    size = models.CharField(max_length=20, null=False, choices=PIZZA_SIZES)
    order_status = models.CharField(max_length=15, choices=STATUS_ORDER_CHOICES, default="Submitted", blank=False)

    class Meta:
        indexes = (
            models.Index(fields=['customer', '-id']),
        )
        ordering = ('-id', )


    def __str__(self):
        return self.customer.first_name+" -> "+self.pizza.name