from django.contrib import admin
from .models import House, Type


class HouseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'type',
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
