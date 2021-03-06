# Generated by Django 2.1.2 on 2018-10-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('street_1', models.CharField(max_length=120)),
                ('street_2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D'), ('4', 'E')], max_length=120)),
                ('postal_code', models.IntegerField()),
            ],
        ),
    ]
