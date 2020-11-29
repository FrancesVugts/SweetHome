from django.contrib import admin
from .models import UserProfile, Subscription


# Class for the representation of the UserProfile model in the admin
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


# Class for the representation of the Subscription model in the admin
class SubsciptionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'house',
    )


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Subscription, SubsciptionAdmin)
