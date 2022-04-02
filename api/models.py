from django.db import models

# Create your models here.


class items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    barcodedata = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    barcode_type = models.CharField(max_length=100)
    weight = models.FloatField(default=0)
    discount = models.FloatField(default=0)


    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    current_user = models.CharField(max_length=100)
    in_use = models.BooleanField(default=False)
    cart_token = models.CharField(max_length=100)
    last_online = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cart_id = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')

    def __str__(self):
        return str(self.id)

