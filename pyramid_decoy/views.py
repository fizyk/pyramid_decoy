from pyramid.httpexceptions import HTTPFound


def redirect_view(request):
    return HTTPFound(location='http://www.example.com')
