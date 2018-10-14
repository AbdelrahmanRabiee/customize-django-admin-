from django.contrib import admin
from django.utils.timezone import now
from . import models
from . import forms
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


    # customize detail view
    # fields = (
    #     ('name', 'email'),
    #     ('city', 'state'),
    #     'country',
    # )
    form = forms.CustomerForm

    # when editing a record you have the choice to duplicate it
    save_as = True
    save_on_top = True



class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['customer', 'customer_name', 'placed_at', 'shipped', 'shipped_at', 'total']
    ordering = ['placed_at',]
    list_editable = ['shipped']
    list_filter = ['shipped', BigOrderFilter]
    search_fields = ['customer__email']
    actions = ['ship']
    date_hierarchy = 'placed_at'

    fieldsets = (
        (None,{
            'fields':(
                ('customer','shipped'),
                ('discount_code','total'),


            )
        }),
        ('Dates',{
            'classes':('collapse',),
            'fields':('placed_at', 'shipped_at'),
        })
    )

    def ship(self, request, queryset):
        queryset.update(
            shipped = True,
            shipped_at = now()
        )

    ship.short_description = 'Make purchase as shipped now'


class PurchaseItemAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'slug'),
        'description',
        ('price', 'location', 'quantity'),
        'featured'
    )
    radio_fields = {
        'featured':admin.HORIZONTAL
    }

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Purchase, PurchaseAdmin)
admin.site.register(models.PurchaseItem, PurchaseItemAdmin)
admin.site.register(models.Product, ProductAdmin)

