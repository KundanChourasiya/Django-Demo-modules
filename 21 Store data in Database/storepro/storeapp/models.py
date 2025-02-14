from django.db import models

class ProductData(models.Model):
    productname=models.CharField(max_length=20)
    productcost=models.IntegerField()
    productcolor=models.CharField(max_length=20)
    productdesc=models.CharField(max_length=50)
