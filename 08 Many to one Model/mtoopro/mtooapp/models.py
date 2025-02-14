from django.db import models

class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=20)
    sloc = models.CharField(max_length=20)
    def __str__(self):
        return self.sname

class Course(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
    cno = models.IntegerField()
    cname = models.CharField(max_length=20)
    cfee = models.IntegerField()
    def __str__(self):
        return self.cname

