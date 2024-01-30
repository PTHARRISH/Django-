from django.db import models

class Position(models.Model):
  title=models.CharField(max_length=50)

  def __str__(self):
    return self.title
  # when you call the foreign key without __str__ it shows (position object1) after declares when ever call the class
  # it will display representation of self.title


class User(models.Model):
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)
  mobile=models.CharField(max_length=10)
  position=models.ForeignKey(Position,on_delete=models.CASCADE)

  def __str__(self):
    return "%s%s"%(self.firstname,self.lastname)
  # display the admin panel show the table name is first and last name or else it shows (user object(1)) by default 

