@when('I edit the serie with name "{name}"')
def step_impl(context, name):
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=name)
    context.browser.visit(context.get_url('fakefilmsweb:serie_edit', serie.pk))
    if context.browser.url == context.get_url('fakefilmsweb:serie_edit', serie.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()