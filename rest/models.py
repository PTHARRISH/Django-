from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=10)
    user=models.CharField(max_length=30)
    password=models.CharField(max_length=10)

    def __str__(self):
        return "%s"%(self.name)