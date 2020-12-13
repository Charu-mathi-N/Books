from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.management import BaseCommand
from decimal import Decimal
import random

def random_string():
    return str(random.randint(250, 500))

random_string = str(random.randint(250, 500))

class Books(models.Model):
    Title = models.CharField(max_length = 100)
    Authors = models.CharField(max_length = 100)
    Rating = models.FloatField(max_length = 3)
    ISBN = models.CharField(max_length = 10)
    ISBN13 = models.CharField(max_length = 10)
    Language = models.CharField(max_length = 5)
    Pages =  models.IntegerField(blank=True, null=True)
    Rating_Count = models.IntegerField()
    Reviews_Count = models.IntegerField()
    Published_Date = models.CharField(max_length = 20)
    Publisher = models.CharField(max_length = 100)
    price = models.IntegerField(default = random_string)
    quantity = models.IntegerField(default=1)


class BookOrder(models.Model):

    def BookOrder(self, bookID):
        book = Books.objects.get(pk=bookID)
    product = models.ForeignKey(Books, null=True, on_delete=models.CASCADE)
    #Cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)

class CustomerPremium(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    stripeid = models.CharField(max_length = 25)
    stripe_subscription_id = models.CharField(max_length = 100)
    cancel = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)

class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField(default=1)
    name = models.CharField(max_length = 50)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=250)




