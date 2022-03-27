from django.db import models

# Create your models here.


class items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    barcodedata = models.CharField(max_length=100)
    price = models.FloatField()
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    barcode_type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)