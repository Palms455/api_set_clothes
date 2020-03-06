from rest_framework import serializers
from .models import Item, ItemSet

class ItemSetSerializer(serializers.Serializer):
	name = serializers.CharField()
	type = serializers.CharField()
	topi = serializers.CharField()
	bottomi = serializers.CharField()
	price = serializers.CharField()

