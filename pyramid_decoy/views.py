# Copyright (c) 2014 by pyramid_decoy authors and contributors
# <see AUTHORS file>
#
# This module is part of pyramid_decoy and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT

from pyramid.httpexceptions import HTTPFound


def decoy(request):
    return HTTPFound(location='http://www.example.com')
