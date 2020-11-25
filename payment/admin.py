from django.contrib import admin
from .models import YearPayment


class YearPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('payment_number', 'date', 'payment_total',)

    fields = ('payment_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'payment_total',)

    list_display = ('payment_number', 'date', 'full_name',
                    'payment_total',)

    ordering = ('-date',)

admin.site.register(YearPayment, YearPaymentAdmin)
