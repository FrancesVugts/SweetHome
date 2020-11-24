from django.db import models
from houses.models import House
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ]


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initials = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=gender_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    country = CountryField(blank_label='Country')
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Subscription(models.Model):
    """
    A subscription model for maintaining wich
    user would like to have a go at wich house
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
