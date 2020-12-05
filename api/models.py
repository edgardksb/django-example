from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    date = models.DateField(default=now)
    time = models.TimeField(default=now)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} to {self.customer.name} at {self.date} {self.time}'
