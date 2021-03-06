from django.db import models
from django_countries.fields import CountryField
from django.utils.timezone import now

# Create your models here.

class Customer(models.Model):
    name        = models.CharField(max_length=120)
    email       = models.EmailField()
    street_1    = models.CharField(max_length=120)
    street_2    = models.CharField(max_length=120, null=True, blank=True)
    city        = models.CharField(max_length=120)
    state       = models.CharField(max_length=120)
    country     = CountryField()
    postal_code = models.IntegerField()

    def __str__(self):
        return self.email

    @property
    def customer_name(self):
        return self.name

class Product(models.Model):
    featured_choices = (
        (0,'A'),
        (1, 'B'),
        (2, 'C')
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.CharField(max_length=10, unique=True)
    quantity = models.IntegerField()
    featured = models.IntegerField(choices=featured_choices)

    class Meta:
        ordering = ['name']

class Purchase(models.Model):
    customer        = models.ForeignKey(Customer, related_name='purchases', on_delete=models.CASCADE)
    placed_at       = models.DateTimeField(default=now)
    shipped_at      = models.DateTimeField(null=True, blank=True)
    discount_code   = models.CharField(blank=True, default='', max_length=20)
    total           = models.DecimalField(max_digits=9, decimal_places=2)
    shipped         = models.BooleanField(default=False)
    items           = models.ManyToManyField(Product, through='PurchaseItem')

    @property
    def customer_name(self):
        return self.customer.name




class PurchaseItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)




