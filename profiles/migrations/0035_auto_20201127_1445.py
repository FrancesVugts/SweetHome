# Generated by Django 3.1.2 on 2020-11-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0034_auto_20201127_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
