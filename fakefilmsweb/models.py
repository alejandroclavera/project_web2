from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Model Distributor
class Distributor(models.Model):
    distributor_name = models.CharField(max_length=30)

    def __str__(self):
        return self.distributor_name

# Model Movie
class Movie(models.Model):
    movie_name= models.CharField(max_length=30)
    movie_category= models.CharField(max_length=50)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

    def average_rating(self):
        review_count = self.moviereview_set.count()
        if not review_count:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.moviereview_set.all()])
            return ratingSum / reviewCount
    def get_absolute_url(self):
        return reverse('fakefilmsweb:movie_list')

# Model Serie
class Serie(models.Model):
    serie_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    number_of_seasons = models.IntegerField(default=1)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.serie_name

    def average_rating(self):
        review_count = self.moviereview_set.count()
        if not review_count:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.moviereview_set.all()])
            return ratingSum / reviewCount

    def get_absolute_url(self):
        return reverse('fakefilmsweb:serie_list')

# Model Episode
class Episode(models.Model):
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    season = models.CharField(max_length=30)
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model User Movie List
class UsersMovieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return str(self.user) + ',' + str(self.movie)

# Model User Serie List
class UsersSerieList(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'serie')
    
    def __str__(self):
        return str(self.user) + ',' + str(self.serie)


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class MovieReview(Review):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("movie", "user")

class SerieReview(Review):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("serie", "user")
