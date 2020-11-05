from django.contrib import admin
from .models import House, Type, City


class HouseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'house_type',
        'address',
        'postal_code',
        'city',
        'price',
        'start_date',
        'end_date',
    )

    ordering = ('-sku',)


admin.site.register(House, HouseAdmin)
admin.site.register(Type)
admin.site.register(City)
