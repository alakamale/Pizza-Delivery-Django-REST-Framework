from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Order, Pizza, Customer, CustomerAddress


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name')
        read_only_fields = ('id',)

    def create(self, validated_data):       
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ('id','customer', 'address')
        read_only_fields = ('id', 'ctime', 'mtime', )

    def create(self, validated_data):        
        customer_id = self.context['view'].kwargs['customer_id']
        return CustomerAddress.objects.create(customer_id=customer_id, **validated_data)

    def update(self, instance, validated_data):        
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name')
        read_only_fields = ('id',)

    def create(self, validated_data):        
        return Pizza.objects.create(**validated_data)

    def update(self, instance, validated_data):       
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_address', 'pizza', 'size', 'order_status')
        read_only_fields = ('id', 'order_status',)

    def validate(self, data):
        customer_address = data['customer_address']
        customer_id = int(self.context['view'].kwargs['customer_id'])

        if customer_address.customer_id != customer_id:
            raise ValidationError(detail='Address not Found')

        return data

    def to_representation(self, instance):
        response = super().to_representation(instance)

        del response['customer_address']
        del response['size']

        response['address'] = CustomerAddressSerializer(instance.customer_address).data

        response['pizza'] = PizzaSerializer(instance.pizza).data
        response['pizza']['size'] = instance.size
        return response

    def create(self, validated_data):       
        customer_id = self.context['view'].kwargs['customer_id']
        return Order.objects.create(customer_id=customer_id, **validated_data)

    def update(self, instance, validated_data):        
        instance.customer_address = validated_data.get('customer_address', instance.customer_address)
        instance.pizza = validated_data.get('pizza', instance.pizza)
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance
