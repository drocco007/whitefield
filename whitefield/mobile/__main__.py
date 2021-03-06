from wsgiref.simple_server import make_server
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # FIXME: can this be done declaratively?
    config.include('whitefield.mobile.auth', route_prefix='/1/auth')
    config.include('whitefield.mobile', route_prefix='/1/schedule')

    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
