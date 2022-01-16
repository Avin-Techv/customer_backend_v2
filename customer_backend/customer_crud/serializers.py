from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer


class UserSerializer(serializers.ModelSerializer):
    customers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Customer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'customers']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
