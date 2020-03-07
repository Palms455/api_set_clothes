from rest_framework import serializers
from .models import Item, ItemSet
from collections import OrderedDict

class ItemSetSerializer(serializers.ModelSerializer):
	type = serializers.CharField()
	items_top = serializers.CharField(source = 'top.name')
	items_bottom = serializers.CharField(source='bottom.name')
	price = serializers.IntegerField()
	class Meta:

		model = ItemSet
		fields = ('name', 'type', 'items_top', 'items_bottom', 'price')
		
	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in ['0', None]])
		
