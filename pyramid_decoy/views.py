from pyramid.httpexceptions import HTTPFound


def decoy(request):
    return HTTPFound(location='http://www.example.com')
