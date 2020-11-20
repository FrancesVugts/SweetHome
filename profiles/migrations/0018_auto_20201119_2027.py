# Generated by Django 3.1.2 on 2020-11-19 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0012_auto_20201105_1241'),
        ('profiles', '0017_auto_20201119_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='house',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.house'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile'),
        ),
    ]
