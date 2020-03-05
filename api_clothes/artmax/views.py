from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, ItemSet, Products
from .serializers import  ItemSerializer, ItemSetSerializer
from django.db.models import Sum


class ItemSetView(APIView):
	def get(self, request):
		prod = Products.objects\
			.filter(item__ItemSet_top__isnull=True)\
			.filter(item__ItemSet_bottom__isnull=True)
		itemserial = []
		sets_query = ItemSet.objects.annotate(price=Sum('top__price') + Sum('bottom__price'))
		for i in prod:
			if Item.objects.filter(name=i.name).exists():
				item = Item.objects.get(name=i.name)
				itemserial.append(ItemSerializer(item).data)
			else:
				sets = sets_query.get(name=i.name)
				itemserial.append(ItemSetSerializer(sets).data)
		return Response(itemserial)
