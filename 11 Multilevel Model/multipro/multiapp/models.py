from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=20)
    sfee = models.IntegerField()
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.sname

class Emp(Student):
    ename = models.CharField(max_length=20)
    esal = models.IntegerField()
    def __str__(self):
        return self.ename

class Customer(Emp):
    cname = models.CharField(max_length=20)
    csale = models.IntegerField()
    def __str__(self):
        return self.cname

