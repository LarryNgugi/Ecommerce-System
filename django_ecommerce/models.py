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
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    location = models.CharField(max_length=100, blank=True, null=False)
    pin = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    orderNumber = models.CharField(max_length=20, blank=False, null=True)
    cost = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=50, null=False, blank=True)
    shippingCost = models.IntegerField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderProduct(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=True)
    quantity = models.CharField(max_length=20, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shipping(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=True)
    customerAddressId = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    mode = models.CharField(max_length=10, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False, null=True)
    invoiceNumber = models.CharField(max_length=10, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    # rating  = models.
    message = models.TextField()
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Wishlist(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Offer(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    offerAmount = models.IntegerField(blank=False, null=False)
    startDate = models.DateTimeField(blank=False, null=True)
    endDate = models.DateTimeField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Voucher(models.Model):
    tag = models.CharField(max_length=50, blank=True, null=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=True)
    amountDeducted = models.IntegerField(default=0, blank=True, null=False)
    status = models.CharField(max_length=50, null=False, blank=True)
    limit = models.DateTimeField(blank=False, null=False)
