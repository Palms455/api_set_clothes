from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, ItemSet
from .serializers import ItemSerializer, ItemSetSerializer
from django.db.models import Sum

class ItemSetView(APIView):
	def get(self, request):
		items = Item.objects.filter(ItemSet_top__isnull=True).filter(ItemSet_bottom__isnull=True)
		sets = ItemSet.objects.annotate(price=Sum('top__price') + Sum('bottom__price'))
		serialize_item = ItemSerializer(items, many=True)
		serialize_set_item = ItemSetSerializer(sets, many=True)
		return Response(serialize_item.data + serialize_set_item.data)
