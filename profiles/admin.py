from django.contrib import admin
from .models import UserProfile


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


admin.site.register(UserProfile, ProfileAdmin)
