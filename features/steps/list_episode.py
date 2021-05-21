from behave import *

use_step_matcher("parse")

@when('I list episode')
def step_impl(context):
    context.browser.visit(context.get_url('fakefilmsweb:episode_list'))

@then('I\'m viewing a list containing')
def step_impl(context):
    episode_links = context.browser.find_by_css('div#content ul li a')
    for i, row in enumerate(context.table):
        assert row['episode_name'] == episode_links[i].text

@step('The list contains {count:n} episode')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li a'))