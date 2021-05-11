from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from fakefilmsweb.models import Movie, MovieReview
from fakefilmsweb.forms import MovieForm

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
    template_name = 'fakefilmsweb/movie_form.html'

# Aplication Views
class CreateMovie(CreateView):
    model = Movie
    template = 'fakefilms/movieForm.html'
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

@login_required()
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if movie.user == request.user:
        movie.delete()
        return HttpResponse('<h1>MOVIE DELETED<h1>')
    else:
        return HttpResponse('<h1>CAN\'T DELETE MOVIE<h1>')

