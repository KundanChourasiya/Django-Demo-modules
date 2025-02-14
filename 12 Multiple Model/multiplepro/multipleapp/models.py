from django.db import models

class Emp(models.Model):
    eid = models.AutoField(primary_key=True)
    eno = models.IntegerField()
    ename = models.CharField(max_length=20)
    esal = models.IntegerField()
    def __str__(self):
        return self.ename

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    cno = models.IntegerField()
    cname = models.CharField(max_length=20)
    csale = models.IntegerField()
    def __str__(self):
        return self.cname

class Student(Emp,Customer):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    sfee = models.IntegerField()
    def __str__(self):
        return self.sname
