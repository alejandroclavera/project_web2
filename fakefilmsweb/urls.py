from django.contrib import admin
from django.urls import path
from django.views.generic import DetailView, ListView
from fakefilmsweb.models import Movie
from fakefilmsweb.views import CreateMovie, InfoMovie, LoginRequiredCheckIsOwnerUpdateView, delete_movie
from fakefilmsweb.forms import MovieForm

app_name = 'fakefilmsweb'

urlpatterns = [
    path('', ListView.as_view(
        queryset=Movie.objects.all(),
        context_object_name='movies_list',
        template_name='fakefilmsweb/movie_list.html'
    ), name='movie_list'),

    path('movie/create', CreateMovie.as_view(), name='create_movie'),
    path('movie/<int:pk>', InfoMovie.as_view(), name='info_movie'),
    path('movie/<int:pk>/edit', 
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model = Movie,
            form_class = MovieForm
        ),
        name='movie_edit'
    ),
    path('movie/<int:pk>/delete', delete_movie, name='movie_delete'),
]