from django.contrib import admin
from django.db.models import Count
from . import models
# Register your models here.

class BigOrderFilter(admin.SimpleListFilter):
    title = 'Big Purchase Total'
    parameter_name = 'big_purchase'

    def lookups(self, request, model_admin):
        return (
            ('1','more than 500'),
            ('2', 'more than 1000'),
            ('3', 'more than 5000'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(total__gte=500)
        elif self.value() == '2':
            return queryset.filter(total__gte=1000)
        elif self.value() == '3':
            return queryset.filter(total__gte=5000)

        return queryset



class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'name', 'email', 'street_1', 'city', 'state', 'country']
    list_editable = ['street_1', ]
    search_fields = ['email', 'name']
    list_filter = ['city']



class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'customer_name', 'placed_at', 'shipped', 'shipped_at', 'total']
    ordering = ['placed_at',]
    list_editable = ['shipped', 'shipped_at']
    list_filter = ['shipped', BigOrderFilter]
    search_fields = ['customer__email']
    date_hierarchy = 'placed_at'


class PurchaseItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
