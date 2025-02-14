from django.db import models

class person(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    def __str__(self):
        return self.name

