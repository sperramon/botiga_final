# -*- coding: utf-8 -*-
from pyramid.config import Configurator
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    settings['mako.directories'] = os.path.join(here, 'templates')
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('inici', '/') #productes=view, /botiga = URL
    config.add_route('productes', '/productes') #productes=view, /botiga = URL
    config.add_route('comanda', '/comanda') #productes=view, /botiga = URL
    config.add_route('fercomanda', '/comanda_feta') #productes=view, /botiga = URL
    config.scan()
    return config.make_wsgi_app()
