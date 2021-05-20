from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from fakefilmsweb.models import *
from django.contrib.auth.models import User
from fakefilmsweb.forms import MovieForm, SerieForm, EpisodeForm

# Requerimets
class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'fakefilmsweb/form.html'

    def get_context_data(self, **kwargs):
        context = super(LoginRequiredCheckIsOwnerUpdateView, self).get_context_data(**kwargs)
        context['TITLE'] = 'EDIT'
        return context

# Aplication Views

# Movies Views
class CreateMovie(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'fakefilmsweb/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMovie, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateMovie, self).get_context_data(**kwargs)
        context['TITLE'] = 'CREATE MOVIE'
        return context

class InfoMovie(DetailView):
    model = Movie
    template_name = 'fakefilmsweb/info_movie.html'

# Series View
class CreateSerie(LoginRequiredMixin, CreateView):
    model = Serie
    template_name = 'fakefilmsweb/form.html'
    form_class = SerieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateSerie, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(CreateSerie, self).get_context_data(**kwargs)
        context['TITLE'] = 'CREATE SERIE'
        return context

class InfoSerie(DetailView):
    model = Serie
    template_name = 'fakefilmsweb/info_serie.html'

@login_required()
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.user == request.user:
        movie.delete()
        return info_status(request, 'MOVIE DELETED')
    else:
        return info_status(request, 'CAN\'T DELETE MOVIE')

@login_required()
def delete_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if serie.user == request.user:
        serie.delete()
        return info_status(request, 'SERIE DELETED')
    else:
        return info_status(request, 'CAN\'T DELETE SERIE')

class CreateEpisode(LoginRequiredMixin, CreateView):
    model = Episode
    template_name = 'fakefilmsweb/form.html'
    form_class = EpisodeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.serie = Serie.objects.get(id=self.kwargs['pk'])
        return super(CreateEpisode, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateEpisode, self).get_context_data(**kwargs)
        context['TITLE'] = 'NEW EPISODE'
        return context

def episode_list(request, pk):
    template = loader.get_template('fakefilmsweb/episode_list.html')
    serie = Serie.objects.get(id=pk)
    document = template.render({'serie':serie, 'episode_list':Episode.objects.all(), 'user':request.user})
    return HttpResponse(document)

def episode_info(request, pk_serie, pk_episode):
    template = loader.get_template('fakefilmsweb/info_episode.html')
    episode = Episode.objects.get(id=pk_episode)
    document = template.render({'episode':episode, 'user':request.user})
    return HttpResponse(document)

class InfoEpisode(DetailView):
    model = Episode
    template_name = 'fakefilmsweb/info_episode.html'

@login_required()
def delete_episode(request, pkr, pk):
    episode = get_object_or_404(Episode, pk=pk)
    if episode.user == request.user:
        episode.delete()
        return info_status(request, 'EPISODE DELETED', next_url='fakefilmsweb:serie_list')
    else:
        return info_status(request, 'CAN\'T DELETE Episode')

@login_required()
def add_movie_to_list(request, pk_user, pk_movie):
    # check if the user is the owner of list
    if request.user.id != pk_user:
         return info_status(request, 'NOT PERMITED USER')
    user = get_object_or_404(User, pk=pk_user)
    movie = get_object_or_404(Movie, pk=pk_movie)
    if not UsersMovieList.objects.filter(user=user, movie=movie).exists():
        movie = UsersMovieList.objects.create(user=user, movie=movie, date=timezone.now())
        return info_status(request, 'MOVIE ADDED')
    else:
        return info_status(request, 'MOVIE IS ALREADY ADDED')

@login_required()
def remove_movie_to_list(request, pk_user, pk_movie):
    # check if the user is the owner of list
    if request.user.id != pk_user:
         return info_status(request, 'NOT PERMITED USER')
    user = get_object_or_404(User, pk=pk_user)
    movie = get_object_or_404(Movie, pk=pk_movie)
    if UsersMovieList.objects.filter(user=user, movie=movie).exists():
        UsersMovieList.objects.get(user=user, movie=movie).delete()
        return info_status(request, 'MOVIE REMOVED')
    else:
       return info_status(request, 'MOVIE NOT FOUND')

@login_required()
def add_serie_to_list(request, pk_user, pk_serie):
    # check if the user is the owner of list
    if request.user.id != pk_user:
         return info_status(request, 'NOT PERMITED USER')
    user = get_object_or_404(User, pk=pk_user)
    serie = get_object_or_404(Serie, pk=pk_serie)
    if not UsersSerieList.objects.filter(user=user, serie=serie).exists():
        UsersSerieList.objects.create(user=user, serie=serie, date=timezone.now())
        return info_status(request, 'SERIE ADDED')
    else:
        return info_status(request, 'SERIE IS ALREADY ADDED')

@login_required()
def remove_serie_to_list(request, pk_user, pk_serie):
    # check if the user is the owner of list
    if request.user.id != pk_user:
         return info_status(request, 'NOT PERMITED USER')
    user = get_object_or_404(User, pk=pk_user)
    serie = get_object_or_404(Serie, pk=pk_serie)
    if UsersSerieList.objects.filter(user=user, serie=serie).exists():
        UsersSerieList.objects.get(user=user, serie=serie).delete()
        return info_status(request, 'SERIE REMOVED')
    else:
        return info_status(request, 'SERIE NOT FOUND')

def info_status(request, message, next_url=None):
    template = loader.get_template('fakefilmsweb/info_status.html')
    if next_url is None:
        next_url = 'fakefilmsweb:movie_list'
    document = template.render({'message':message, 'user':request.user, 'next':reverse(next_url),})
    return HttpResponse(document)

