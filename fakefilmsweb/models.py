from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Model Movie
class Movie(models.Model):
    movie_name= models.CharField(max_length=30)
    movie_category= models.CharField(max_length=50)
    year = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('fakefilmsweb:movie_list')

# Model Serie
class Serie(models.Model):
    serie_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    number_of_seasons = models.IntegerField(default=1)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.serie_name

    def get_absolute_url(self):
        return reverse('fakefilmsweb:serie_list')

# Model Episode
class Episode(models.Model):
    serie = models.ForeignKey(Serie, related_name='episodes', on_delete=models.CASCADE)
    season = models.CharField(max_length=30)
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('fakefilmsweb:info_episode', kwargs={'pks':self.serie.pk, 'pk': self.pk})

# Model User Movie List
class UsersMovieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'movie')

    def get_absolute_url(self):
        return reverse('fakefilmsweb:serie_list')

    def __str__(self):
        return str(self.user) + ',' + str(self.movie)

# Model User Serie List
class UsersSerieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'serie')

    def get_absolute_url(self):
        return reverse('fakefilmsweb:serie_list')
    
    def __str__(self):
        return str(self.user) + ',' + str(self.serie)
