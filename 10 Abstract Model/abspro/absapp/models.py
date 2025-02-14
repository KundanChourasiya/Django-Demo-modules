from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Student(CommonInfo):
    fee =models.IntegerField()
    def __str__(self):
        return self.name

class Emp (CommonInfo):
    sal = models.IntegerField()
    def __str__(self):
        return self.name

class Customer(CommonInfo):
    saleamt = models.IntegerField()
    def __str__(self):
        return self.name
