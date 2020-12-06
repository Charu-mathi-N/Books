from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.management import BaseCommand
from decimal import Decimal

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
    price = models.FloatField(default = 250)
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


'''class Cart(models.Model):

    def __init__(self, request):
        """
        Initialize the cart.
        """

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        print("Item Added to cart")
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        print("Item Added to cart")
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()'''


    # def remove(self, product):
    #         """
    #         Remove a product from the cart.
    #         """
    #         product_id = str(product.id)
    #         if product_id in self.cart:
    #             del self.cart[product_id]
    #             self.save()

    # def decrement(self, product):
    #     for key, value in self.cart.items():
    #         if key == str(product.id):

    #             value['quantity'] = value['quantity'] - 1
    #             if(value['quantity'] < 1):
    #                 return redirect('main:home')
    #             self.save()
    #             break
    #         else:
    #             print("Something Wrong")

    # def clear(self):
    #     # empty cart
    #     self.session[settings.CART_SESSION_ID] = {}
    #     self.session.modified = True


