from behave import *

use_step_matcher("parse")

@when('I list serie')
def step_impl(context):
    context.browser.visit(context.get_url('fakefilmsweb:serie_list'))

@then('I\'m viewing a list containing')
def step_impl(context):
    serie_links = context.browser.find_by_css('div#content ul li a')
    for i, row in enumerate(context.table):
        assert row['serie_name'] == serie_links[i].text

@step('The list contains {count:n} series')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li a'))