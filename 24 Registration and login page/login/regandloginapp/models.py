from django.db import models

class  Reg(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    user = models.CharField(max_length=20, primary_key=True)
    pwd = models.CharField(max_length=20)
    mobile = models.IntegerField(max_length=10,unique=True)
    email = models.EmailField(max_length=20,unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.fname

