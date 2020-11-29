import uuid

from django.db import models


# A model for all the YearPayment information
class YearPayment(models.Model):
    payment_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    payment_total = models.DecimalField(null=False, editable=False, max_digits=10, decimal_places=2)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_payment_number(self):
        # Generate a random, unique number using UUID
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        # Override the original save method to set the payment number
        # if it hasn't been set already.
        if not self.payment_number:
            self.payment_number = self._generate_payment_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_number
