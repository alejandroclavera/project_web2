@when('I edit the movie with name "{name}"')
def step_impl(context, name):
    from fakefilmsweb.models import Movie
    movie = Movie.objects.get(movie_name=name)
    context.browser.visit(context.get_url('fakefilmsweb:movie_edit', movie.pk))
    if context.browser.url == context.get_url('fakefilmsweb:movie_edit', movie.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()