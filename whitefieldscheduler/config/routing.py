"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect("schedule", "/schedule/{school}/{title}", controller="day",
                action="json")

    map.connect("schedule", "/{school}/{title}", controller="day",
                action="show")

    map.connect("schedule", "/{title}", controller="day", school="us",
                action="show")

    map.connect("schedule", "/{school}/", controller="day", title="today",
                action="show")

    map.connect("schedule", "/", controller="day", action="show", title="today", school="us")

    return map
