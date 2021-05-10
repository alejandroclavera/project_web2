from django.forms import ModelForm
from fakefilmsweb.models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('user', 'date',)