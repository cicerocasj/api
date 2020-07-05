from django.utils.timezone import now
from django.db.models.signals import post_save
from django.db import models
from django.db.models import Sum


ORDER_STATUS_CHOICES = (
    (1, 'stock'),
    (2, 'transferring'),
    (3, 'delivered'),
    (4, 'canceled'),
)


class Client(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    birth = models.DateTimeField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField()

    def __str__(self):
        return '%s - %s' % (self.name, self.value)


class Order(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    total_value = models.FloatField(null=True)
    date_order = models.DateTimeField(default=now)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)

    def __str__(self):
        return '%s - %s' % (self.id, self.client)


def set_total_value_order(sender, instance, **kwargs):
    instance.total_value = instance.products.aggregate(total=Sum('value')).get('total')


post_save.connect(set_total_value_order, sender=Order)
