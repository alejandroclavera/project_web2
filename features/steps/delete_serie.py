@when('I delete the serie with name "{name}"')
def step_impl(context, name):
    from fakefilmsweb.models import Serie
    serie = Serie.objects.get(serie_name=name)
    context.browser.visit(context.get_url('fakefilmsweb:info_serie', serie.pk))
    if context.browser.url == context.get_url('fakefilmsweb:info_serie', serie.pk):
        context.browser.find_by_value('remove').first.click()