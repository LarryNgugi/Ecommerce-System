from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Seller(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=False, null=False)
    business_reg_no = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=True)
    email = models.EmailField(max_length=50, blank=False, null=False)
    external_url = models.SlugField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=False)
    image_url = models.ImageField()
    price = models.IntegerField(blank=False, null=False)
    inventory = models.CharField(max_length=50, blank=False, null=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerAddress(models.Model):
    customer_id = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, null=False)
    pin = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


