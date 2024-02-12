from django.db import models

# harrishpt
# admin@123
# Create your models here.
class Color(models.Model):
    color_name=models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.color_name)
    
class User(models.Model):
    name = models.CharField(max_length=10)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    color=models.ForeignKey(Color,null=True,blank=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return "%s" % (self.name)
    

