from django.db import models

# Create your models here.
class jkkonline(models.Model):
    jenis_kitab = models.CharField(max_length=255)
    harga_barang = models.CharField(max_length=255)
