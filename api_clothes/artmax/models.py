from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=150, verbose_name='Наменование')
	type = models.CharField(max_length=10, verbose_name='Тип товара', choices=(('top', 'Верх'), ('bottom', 'Низ'), ('not select', 'Не выбрано')))
	price = models.IntegerField(verbose_name='Цена')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'		

	def __str__(self):
		return self.name


class ItemSet(models.Model):
	name = models.CharField(max_length= 150, verbose_name='Наименование набора')
	top = models.OneToOneField(Item, limit_choices_to={'type': 'top', 'ItemSet_top__isnull': True }, verbose_name='Верх', on_delete=models.CASCADE, related_name='ItemSet_top')
	bottom = models.OneToOneField(Item, limit_choices_to={'type': 'bottom', 'ItemSet_bottom__isnull': True}, verbose_name= 'Низ', on_delete=models.CASCADE, related_name='ItemSet_bottom')

	class Meta:
		verbose_name = 'Набор'
		verbose_name_plural = 'Наборы'

	def __str__(self):
		return self.name
