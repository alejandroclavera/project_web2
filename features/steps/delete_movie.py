@when('I delete the movie with name "{name}"')
def step_impl(context, name):
    from fakefilmsweb.models import Movie
    movie = Movie.objects.get(movie_name=name)
    context.browser.visit(context.get_url('fakefilmsweb:info_movie', movie.pk))
    if context.browser.url == context.get_url('fakefilmsweb:info_movie', movie.pk):
        context.browser.find_by_value('remove').first.click()