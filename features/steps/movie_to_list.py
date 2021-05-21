from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@when('When I add a movie to my list with the name "{name}"')
def step_impl(context,user,name):
    from fakefilmsweb.models import Movie, UsersMovieList, User
    movie = Movie.objects.get(movie_name=name)
    user = User.objects.get(username=username)
    context.browser.visit(context.get_url('fakefilmsweb:movie_list'))
    if context.browser.url == context.get_url('fakefilmsweb:movie_list'):
        add_button = context.browser.find_by_tag('img')
        add_button.click()

@then('I am viewing the details page for my movies by "{name}"')
    def step_impl(context,user):
        from fakefilmsweb.models import Movie, UsersMovieList, User
        user = User.objects.get(username=username)
        context.browser.visit(context.get_url('fakefilmsweb:movie_user_list', user.pk))

@then('There are {count:n} movie')
    def step_impl(context,count):
        



