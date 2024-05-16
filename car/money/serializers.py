from rest_framework import serializers
from .models import *


class CarorSparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarorSpareparts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


