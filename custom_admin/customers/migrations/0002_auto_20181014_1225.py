# Generated by Django 2.1.2 on 2018-10-14 12:25

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
