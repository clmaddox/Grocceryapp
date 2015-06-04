from django.contrib import admin

from .models import ShoppingList, Item

class ItemInline(admin.TabularInline):
	model = Item
	extra = 1

class ShoppingListAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['list_name']})]
	inlines = [ItemInline]

admin.site.register(ShoppingList, ShoppingListAdmin)
