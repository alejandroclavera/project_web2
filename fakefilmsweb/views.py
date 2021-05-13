from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from fakefilmsweb.models import Movie, MovieReview, Serie, SerieReview
from fakefilmsweb.forms import MovieForm, SerieForm

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

# Aplication Views

# Movies Views
class CreateMovie(CreateView):
    model = Movie
    template_name = 'fakefilmsweb/form.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMovie, self).form_valid(form)

class InfoMovie(DetailView):
    model = Movie
    template_name = 'fakefilmsweb/info_movie.html'

    def get_context_data(self, **kwargs):
        context = super(InfoMovie, self).get_context_data(**kwargs)
        context['RATING'] = MovieReview.RATING_CHOICES
        return context

# Series View
class CreateSerie(CreateView):
    model = Serie
    template_name = 'fakefilmsweb/form.html'
    form_class = SerieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateSerie, self).form_valid(form)

class InfoSerie(DetailView):
    model = Serie
    template_name = 'fakefilmsweb/info_serie.html'

    def get_context_data(self, **kwargs):
        context = super(InfoSerie, self).get_context_data(**kwargs)
        context['RATING'] = SerieReview.RATING_CHOICES
        return context


@login_required()
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.user == request.user:
        movie.delete()
        return HttpResponse('<h1>MOVIE DELETED<h1>')
    else:
        return HttpResponse('<h1>CAN\'T DELETE MOVIE<h1>')

@login_required()
def delete_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    if serie.user == request.user:
        serie.delete()
        return HttpResponse('<h1>Serie DELETED<h1>')
    else:
        return HttpResponse('<h1>CAN\'T DELETE Serie<h1>')
