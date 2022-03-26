from rest_framework import serializers
from .models import items


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = '__all__'

