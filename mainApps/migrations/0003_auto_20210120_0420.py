# Generated by Django 3.1.2 on 2021-01-19 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApps', '0002_auto_20210120_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='favoriteKitchen',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='mainApps.kitchen'),
        ),
    ]
