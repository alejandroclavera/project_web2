from behave import *

use_step_matcher("parse")

@then('I list episode "{serie_name}"')
def step_impl(context, serie_name):
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=serie_name)
    context.browser.visit(context.get_url('fakefilmsweb:info_serie', serie.pk))

@then('Viewing a list episodes that containing')
def step_impl(context):
    episode_links = context.browser.find_by_css('.episode-element')
    for i, row in enumerate(context.table):
        assert row['name'] == episode_links[i].text

@step('The list contains {count:n} episodes')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('.episode-element'))