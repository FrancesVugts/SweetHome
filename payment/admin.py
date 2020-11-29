from django.contrib import admin
from .models import YearPayment


class YearPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'payment_number', 'date', 'payment_total',
                       'stripe_pid',)

    fields = ('user', 'payment_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'city', 'street_address1',
              'street_address2', 'payment_total',
              'stripe_pid',)

    list_display = ('user', 'payment_number', 'date', 'full_name',
                    'payment_total',)

    ordering = ('-date',)

admin.site.register(YearPayment, YearPaymentAdmin)
