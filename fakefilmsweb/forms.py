from django.forms import ModelForm
from fakefilmsweb.models import Movie, Serie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date',)

class SerieForm(ModelForm):
    class Meta:
        model = Serie
        exclude = ('user', 'date',)