
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, ItemSet
from .serializers import  ItemSetSerializer
from django.db.models import F, Value, IntegerField, CharField

class ItemSetView(APIView):
	def get(self, request):
		item = Item.objects.filter(ItemSet_top__isnull=True)\
			.filter(ItemSet_bottom__isnull=True)\
			.annotate(items_top= Value(0, IntegerField()),
				items_bottom= Value(0, IntegerField()))
		

		sets = ItemSet.objects.all().only('name')\
			.annotate(type = Value('0', CharField()),
			 	price = F('top__price') + F('bottom__price'),
			 	items_top=F('top'), items_bottom=F('bottom'))
			

		all_product = sets.union(item)
		serialize_all_item = ItemSetSerializer(all_product, many=True)
		return Response(serialize_all_item.data)
	