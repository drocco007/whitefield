import datetime
from pyramid.renderers import JSON


def includeme(config):
    config.add_route('schedule', '/')
    config.add_route('schedule:date', '/{date}')

    config.add_route('root', '/')
    config.add_static_view(name='/', path='whitefield.mobile:static')

    config.scan('whitefield.mobile.views')
    json_renderer = JSON()

    def string_adapter(obj, request):
        return str(obj)

    json_renderer.add_adapter(datetime.date, string_adapter)
    json_renderer.add_adapter(datetime.datetime, string_adapter)
    config.add_renderer('json', json_renderer)
