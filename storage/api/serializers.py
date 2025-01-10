from rest_framework import serializers
from .models import Location, Item


class ItemSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location_name.location_name')

    class Meta:
        model = Item
        fields = ['id', 'name', 'date_added', 'location_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

