from .settings import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['fakefilms.herokuapp.com']

# Configure Django App for Heroku.
django_heroku.settings(locals())
