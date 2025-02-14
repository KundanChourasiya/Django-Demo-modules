from django.db import models

class Publisher(models.Model):
    pname = models.CharField(max_length=20)
    ploc = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    def __str__(self):
        return self.pname

class Author(models.Model):
    aname = models.CharField(max_length=20)
    aloc = models.CharField(max_length=20)
    aincome = models.IntegerField()
    def __str__(self):
        return self.aname

class Student(models.Model):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sfee = models.IntegerField()
    def __str__(self):
        return self.sname

class Book(models.Model):
    publisher = models.OneToOneField(Publisher,on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True)
    student = models.ManyToManyField(Student)
    bname = models.CharField(max_length=20)
    bcost = models.IntegerField()
    def __str__(self):
        return self.bname