from django.contrib import admin
from django.urls import path
from django.views.generic import DetailView, ListView
from fakefilmsweb.models import *
from fakefilmsweb.views import *
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
        ), name='serie_edit'),
    path('serie/<int:pk>/delete', delete_serie, name='serie_delete'),

    #Episodes paths
    path('serie/<int:pk>/episode/create', CreateEpisode.as_view(), name='episode_create'),
    path('serie/<int:pks>/episode/<int:pk>', DetailView.as_view(
        model=Episode,
        template_name='fakefilmsweb/info_episode.html'
    ), name='info_episode'),
    path('serie/<int:pks>/episode/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Episode,
            form_class=EpisodeForm),
         name='episode_edit'),

    path('serie/<int:pkr>/episode/<int:pk>/delete', delete_episode, name='episode_delete'),

    # Movie user List paths
    path('user/<int:pk>/movies', ListView.as_view(
        queryset=UsersMovieList.objects.all(),
        context_object_name='movies_list',
        template_name='fakefilmsweb/movie_user_list.html'
    ), name='movie_user_list'),

    path('user/<int:pk_user>/movie/<int:pk_movie>/add', add_movie_to_list, name='movie_list_add'),
    path('user/<int:pk_user>/movie/<int:pk_movie>/delete', remove_movie_to_list, name='movie_list_delete'),

    # serie user List paths
    path('user/<int:pk>/series', ListView.as_view(
        queryset=UsersSerieList.objects.all(),
        context_object_name='serie_list',
        template_name='fakefilmsweb/serie_user_list.html'
    ), name='serie_user_list'),

    path('user/<int:pk_user>/serie/<int:pk_serie>/add', add_serie_to_list, name='serie_list_add'),
    path('user/<int:pk_user>/serie/<int:pk_serie>/delete', remove_serie_to_list, name='serie_list_delete'),
]