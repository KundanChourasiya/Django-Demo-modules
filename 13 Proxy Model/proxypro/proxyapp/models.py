from django.db import models

class Student (models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    sloc = models.CharField(max_length=20)
    def __str__(self):
        return self.sname

class StudentProxy(Student):
    class Meta:
        proxy = True

