from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists serie registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from fakefilmsweb.models import Serie
    for row in context.table:
        serie = Serie(user=user)
        for heading in row.headings:
            setattr(serie, heading, row[heading])
        serie.save()

@when('I register serie')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('fakefilmsweb:create_serie'))
        if context.browser.url == context.get_url('fakefilmsweb:create_serie'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} serie')
def step_impl(context, count):
    from fakefilmsweb.models import Serie
    assert count == Serie.objects.count()

@then('I\'m viewing the details page for serie by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from fakefilmsweb.models import Serie
    serie = Serie.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(serie)