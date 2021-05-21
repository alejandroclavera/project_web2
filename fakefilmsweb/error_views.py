from fakefilmsweb.views import info_status


def error_403(request, exception):
    return info_status(request, '403 Forbidden')


def error_404(request, exception):
    return info_status(request, 'Error 404')