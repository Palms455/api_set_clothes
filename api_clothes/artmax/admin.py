from django.contrib import admin
from .models import Item, ItemSet

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	'''справочники'''
	list_display=('name', 'type', 'price')

class ItemSetAdmin(admin.ModelAdmin):
	list_display=('name', 'top', 'bottom')

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemSet, ItemSetAdmin)
