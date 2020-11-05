from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class City(models.Model):

    class Meta:
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class House(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    photo_1 = models.ImageField(null=True, blank=True)
    photo_2 = models.ImageField(null=True, blank=True)
    photo_3 = models.ImageField(null=True, blank=True)
    photo_4 = models.ImageField(null=True, blank=True)
    photo_5 = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=254)
    postal_code = models.CharField(max_length=254)
    city = models.ForeignKey('City', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    house_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    bedrooms = models.IntegerField(null=True, blank=True)
    construction_year = models.IntegerField(null=True, blank=True)
    energy_label = models.CharField(max_length=254, null=True, blank=True)
    m2 = models.IntegerField(null=True, blank=True)
    m3 = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.address
