from behave import *

use_step_matcher("parse")

@when('I view the details for episode "{episode_name}"')
def step_impl(context, episode_name):
    from fakefilmsweb.models import Episode
    episode = Episode.objects.get(episode_name=episode_name)
    context.browser.visit(context.get_url('fakefilmsweb:info_episode', episode.pk))

@then("I'm viewing episode details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])