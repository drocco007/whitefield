import datetime
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import JSON


def schedule_include(config):
    config.add_route('schedule', '/')
    config.add_route('schedule:date', '/{date}')


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.include(schedule_include, route_prefix='/1/schedule')
    config.add_route('root', '/')
    config.add_static_view(name='/', path='whitefield.mobile:static')

    config.scan('whitefield.mobile.views')
    json_renderer = JSON()

    def string_adapter(obj, request):
        return str(obj)

    json_renderer.add_adapter(datetime.date, string_adapter)
    json_renderer.add_adapter(datetime.datetime, string_adapter)
    config.add_renderer('json', json_renderer)

    # FIXME: can this be done declaratively?
    config.include('whitefield.auth')

    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
