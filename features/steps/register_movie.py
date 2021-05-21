from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists movie registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from fakefilmsweb.models import Movie
    for row in context.table:
        movie = Movie(user=user)
        for heading in row.headings:
            setattr(movie, heading, row[heading])
        movie.save()

@when('I register movie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('fakefilmsweb:create_movie'))
        if context.browser.url == context.get_url('fakefilmsweb:create_movie'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} movie')
def step_impl(context, count):
    from fakefilmsweb.models import Movie
    assert count == Movie.objects.count()

@then('I\'m viewing the details page for movie by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from fakefilmsweb.models import Movie
    movie = Movie.objects.filter(reduce(operator.and_, q_list)).get()
    print(context.browser.url)
    print(context.get_url(movie))
    assert context.browser.url == context.get_url(movie)

