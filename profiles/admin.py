from django.contrib import admin
from .models import UserProfile, Subscription


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'address',
        'postcode',
        'city',
        'country',
        'email',
        'phone_number',
    )


class SubsciptionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'house',
    )


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Subscription, SubsciptionAdmin)
