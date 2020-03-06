
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, ItemSet
from .serializers import  ItemSetSerializer
from django.db.models import Sum

class ItemSetView(APIView):
	def get(self, request):
		item = Item.objects.filter(ItemSet_top__isnull=True).filter(ItemSet_bottom__isnull=True).annotate(topi= Value(False, BooleanField()), bottomi= Value(False, BooleanField())).values('name', 'type', 'price', 'topi', 'bottomi')
		sets = ItemSet.objects.all().only('name').annotate(type = Value(False, BooleanField()), price = F('top__price') + F('bottom__price'), topi=F('top'), bottomi=F('bottom')).values('name', 'type', 'price', 'topi', 'bottomi')
		all_product = sets.union(item)
		#serialize_all_item = ItemSetSerializer(all_product, many=True)
		#return Response(serialize_all_item.data)
		serial = []
		for i in all_product:
			serial.append(ItemSetSerializer(i).data)
		return Response(serial)
		