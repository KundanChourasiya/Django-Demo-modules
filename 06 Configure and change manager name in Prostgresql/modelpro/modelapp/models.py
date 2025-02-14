from django.db import models

class Emp(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    sal = models.IntegerField()
    email = models.EmailField(max_length=200)
    sunny = models.Manager()

    def __str__(self):
        return self.ename
