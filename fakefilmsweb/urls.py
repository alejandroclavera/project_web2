from django.contrib import admin
from django.urls import path
from django.views.generic import DetailView, ListView
from fakefilmsweb.models import Movie, Serie
from fakefilmsweb.views import CreateMovie, InfoMovie, LoginRequiredCheckIsOwnerUpdateView, delete_movie, CreateSerie, InfoSerie, delete_serie
from fakefilmsweb.forms import MovieForm, SerieForm

app_name = 'fakefilmsweb'

urlpatterns = [
    # Path movies
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

    # Path series
    path('serie/list', ListView.as_view(
        queryset=Serie.objects.all(),
        context_object_name='serie_list',
        template_name='fakefilmsweb/serie_list.html'
    ), name='serie_list'),
    path('serie/create', CreateSerie.as_view(), name='create_serie'),
    path('serie/<int:pk>', InfoSerie.as_view(), name='info_serie'),
    path('serie/<int:pk>/edit', 
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model = Serie,
            form_class = SerieForm
        ),
        name='serie_edit'
    ),
    path('serie/<int:pk>/delete', delete_serie, name='serie_delete'),
]