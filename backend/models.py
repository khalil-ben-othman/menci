from django.db import models
from datetime import datetime

class Image(models.Model):
    src = models.ImageField(upload_to='static/assets')
    
    def __str__(self):
        return f"{self.src}"
        
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    old_price = models.PositiveBigIntegerField(blank=True, null=True)
    description = models.TextField(max_length=1000)
    images = models.ManyToManyField(Image)
    sold_out = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    city = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    price = models.PositiveBigIntegerField(default=0)
    size = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.product}({self.size}) x {self.quantity}"

class Subscriber(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.client}-{self.date.strftime('%Y/%m/%d')}"

class Message(models.Model):
    sender_first_name = models.CharField(max_length=1000, default='')
    sender_last_name = models.CharField(max_length=1000, default='')
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender_first_name}-{self.date.strftime('%Y/%m/%d')}"