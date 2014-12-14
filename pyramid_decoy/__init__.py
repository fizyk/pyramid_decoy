# Copyright (c) 2014 by pyramid_decoy authors and contributors
# <see AUTHORS file>
#
# This module is part of pyramid_decoy and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT

import logging

__version__ = '0.0.0'


logger = logging.getLogger(__name__)


def includeme(configurator):
    """
    Configure decoy plugin on pyramid application.

    :param pyramid.configurator.Configurator configurator: pyramid's
        configurator object
    """
    configurator.add_route('decoy', '/')
    configurator.add_view('pyramid_decoy.views.decoy', route_name='decoy')
    # TODO:
    # 1. Read config. - redir address
    # 2. Add redirecting view (root) to redir address read from config
    # 3. Test solution
