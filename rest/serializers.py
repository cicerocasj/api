from rest_framework import serializers
from . import models


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    total_value = serializers.FloatField(required=False)
    client_id = serializers.PrimaryKeyRelatedField(source='client', queryset=models.Client.objects.all())
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Product.objects.all())

    class Meta:
        model = models.Order
        fields = ["id", "url", "total_value", "client_id", "products", "date_order", "status"]
