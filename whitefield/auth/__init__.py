from sqlalchemy import engine_from_config


def init_db(config):
    from . import model

    engine = engine_from_config(config.get_settings(), 'sqlalchemy.')
    model.DBSession.configure(bind=engine)
    model.Base.metadata.bind = engine


def init_routes(config):
    config.add_route('login', '/login', request_method='POST')
    config.add_route('update_user', '/users', request_method='POST')

    config.scan('whitefield.auth.views')


def includeme(config):
    init_db(config)
    init_routes(config)
