from django.contrib import admin
from .models import Item, ItemSet
from django.db.models import F

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	'''справочники'''
	list_display=('name', 'type', 'price')

class ItemSetAdmin(admin.ModelAdmin):
	list_display=['name', 'top', 'bottom', 'price']

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.annotate(price = F('top__price') + F('bottom__price'))

	def price(self, inst):
		return inst.price

	



admin.site.register(Item, ItemAdmin)
admin.site.register(ItemSet, ItemSetAdmin)
