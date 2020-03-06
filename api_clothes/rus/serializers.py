from rest_framework import serializers
from .models import Item, ItemSet

class ItemSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ('name', 'type', 'price')


class ItemSetSerializer(serializers.ModelSerializer):
	top = serializers.CharField(source='top.name')
	bottom = serializers.CharField(source='bottom.name')
	price = serializers.CharField()

	class Meta:
		model = ItemSet
		fields = ('name', 'top', 'bottom', 'price')