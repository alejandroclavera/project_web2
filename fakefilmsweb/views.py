from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from fakefilmsweb.models import Movie
from fakefilmsweb.forms import MovieForm

# Aplication Views
class CreateMovie(CreateView):
    model = Movie
    template = 'fakefilms/movieForm.html'
    form_class = MovieForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMovie, self).form_valid(form)
