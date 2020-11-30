from django.test import TestCase
from houses.models import City, Type, House


class TestModels(TestCase):

    def setUp(self):
        self.type1 = Type.objects.create(
            name='house'
        )

        self.city1 = City.objects.create(
            name='Boxtel'
        )

        self.house1 = House.objects.create(
            sku='h202000001',
            address='address 1',
            postal_code='5283JT',
            city=self.city1,
            price=900.00,
            house_type=self.type1,
            bedrooms=3,
            construction_year=2000,
            energy_label='A',
            m2=80,
            m3=160,
            start_date='2020-11-24',
            end_date='2020-12-24',
            description='description 1',
            photo_1='house/house-front.jpg',
            photo_2='house/house-living.jpg',
            photo_3='house/house-kitchen.jpg',
            photo_4='house/house-bedroom.jpg',
            photo_5='house/house-garden.jpg'
        )

    def test_type_is_assigned_name_on_creation(self):
        self.assertEquals(self.type1.name, 'house')

    def test_city_is_assigned_name_on_creation(self):
        self.assertEquals(self.city1.name, 'Boxtel')

    def test_house_is_assigned_address_on_creation(self):
        self.assertEquals(self.house1.address, 'address 1')
