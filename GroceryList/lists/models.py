from django.db import models

class ShoppingList(models.Model):
	list_name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.list_name

class Item(models.Model):
	shopping_list = models.ForeignKey(ShoppingList)
	item_text = models.CharField(max_length=200)
	item_price = models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		return self.item_text

