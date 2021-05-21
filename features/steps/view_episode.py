from behave import *

use_step_matcher("parse")

@then('I view the details for episode "{episode_name}"')
def step_impl(context, episode_name):
    from fakefilmsweb.models import Serie, Episode
    episode = Episode.objects.get(name=episode_name)
    serie = Serie.objects.get(pk=episode.serie.pk)
    context.browser.visit(context.get_url('fakefilmsweb:info_episode', serie.pk, episode.pk))

@then("I'm viewing episode details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])