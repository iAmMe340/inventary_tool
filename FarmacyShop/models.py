from django.db import models

# Create your models here.
class Proveedor(models.Model):
    cod_proveedor = models.CharField(max_length=8, primary_key=True)



class Product(models.Model):
    cod_producto=models.CharField(max_length=8 , primary_key=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)


class Stock(models.Model):
    cod_producto=models.ForeignKey(Product, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=50, blank=True)
