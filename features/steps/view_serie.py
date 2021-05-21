from behave import *

use_step_matcher("parse")

@when('I view the details for serie "{serie_name}"')
def step_impl(context, serie_name):
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=serie_name)
    context.browser.visit(context.get_url('fakefilmsweb:info_serie', serie.pk))

@then("I'm viewing serie details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])