from django.db import models

from django.contrib.auth.models import User


class SalesPerson(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Customer(models.Model):
    customer = models.ForeignKey(User, related_name='customer')
    sales_person = models.ForeignKey(User, related_name='sales_person')

    def __unicode__(self):
        return self.customer.username


class ItemBrandObject(models.Model):
    name = models.CharField(max_length=50, verbose_name='Display Name')
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Transactions(models.Model):
    transaction_time = models.TimeField(auto_now_add=True)
    product = models.ForeignKey(ItemBrandObject)
    sales_person = models.ForeignKey(User, related_name='transactions')
    customer = models.ForeignKey(User, related_name='purchases')
    cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __unicode__(self):
        return self.product.name

