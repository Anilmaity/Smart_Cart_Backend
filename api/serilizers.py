from rest_framework import serializers
from .models import items, Cart


class itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


