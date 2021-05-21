from functools import reduce

from behave import *
import operator
from django.db.models import Q
import os

from fakefilms.settings import BASE_DIR

use_step_matcher("parse")

@given('Exists episode at serie by "{username}"')
def step_impl(context, serie_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=serie_name)
    from fakefilmsweb.models import Episode
    for row in context.table:
        episode = Episode(serie=serie, user=user)
        for heading in row.headings:
            setattr(episode, heading, row[heading])
        episode.save()

@when('I register episode at serie "{serie_name}"')
def step_impl(context, serie_name):
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=serie_name)
    for row in context.table:
        context.browser.visit(context.get_url('fakefilmsweb:episode_create', serie.pk))
        if context.browser.url == context.get_url('fakefilmsweb:episode_create', serie.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                    context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for episode at serie "{serie_name}" by "{username}"')
def step_impl(context, serie_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from fakefilmsweb.models import Serie
    q_list.append(Q(('serie', Serie.objects.get(name=serie_name))))
    from fakefilmsweb.models import Episode
    episode = Episode.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(episode)
    if episode.image:
        episode.image.delete()

@then('There are {count:n} episodes')
def step_impl(context, count):
    from fakefilmsweb.models import Episode
    assert count == Episode.objects.count()

@when('I edit the current episode')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('fakefilmsweb:episode_edit', episode.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()