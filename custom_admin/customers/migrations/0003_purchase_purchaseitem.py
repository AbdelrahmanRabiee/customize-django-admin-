# Generated by Django 2.1.2 on 2018-10-14 12:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20181014_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('shipped_at', models.DateTimeField(blank=True, null=True)),
                ('discount_code', models.CharField(blank=True, default='', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shipped', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Purchase')),
            ],
        ),
    ]
