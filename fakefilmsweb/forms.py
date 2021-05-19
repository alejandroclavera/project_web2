from django.forms import ModelForm
from fakefilmsweb.models import Movie, Serie, Episode

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date',)

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        exclude = ('user', 'date',)

class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        exclude = ('serie','user','date')