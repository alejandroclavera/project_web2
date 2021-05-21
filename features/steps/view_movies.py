from behave import *

use_step_matcher("parse")

@when('I view the details for movie "{movie_name}"')
def step_impl(context, movie_name):
    from fakefilmsweb.models import Movie
    movie = Movie.objects.get(movie_name=movie_name)
    context.browser.visit(context.get_url('fakefilmsweb:info_movie', movie.pk))

@then("I'm viewing movie details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])