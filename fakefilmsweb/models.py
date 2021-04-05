from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=30)
    def __str__(self):
        return self.distributor_name

class Movie(models.Model):
    movie_name= models.CharField(max_length=30)
    movie_category= models.CharField(max_length=50)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

class Serie(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    number_of_seasons = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Episode(models.Model):
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    season = models.CharField(max_length=30)
    number = models.IntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class UsersMovieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return str(self.user) + ',' + str(self.movie)

class UsersSerieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'serie')
    
    def __str__(self):
        return str(self.user) + ',' + str(self.serie)
