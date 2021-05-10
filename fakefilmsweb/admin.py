from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Distributor)
admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(Episode)
admin.site.register(UsersMovieList)
admin.site.register(UsersSerieList)
admin.site.register(MovieReview)
admin.site.register(SerieReview)
