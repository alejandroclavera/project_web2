from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    date = models.DateTimeField()
    email = models.EmailField()
   
    def __str__(self):
        return self.user_name


class Series(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    seasons = models.IntegerField()

    def __str__(self):
        return self.name
