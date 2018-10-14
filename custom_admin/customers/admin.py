from django.contrib import admin
from . import models
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'name', 'email', 'street_1', 'city', 'state', 'country']
    list_editable = ['street_1', ]


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'customer_name', 'placed_at', 'shipped', 'shipped_at', 'total']
    ordering = ['placed_at',]
    list_editable = ['shipped', 'shipped_at']
    list_filter = ['shipped', 'total']


class PurchaseItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
