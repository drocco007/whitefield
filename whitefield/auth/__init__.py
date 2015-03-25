from sqlalchemy import engine_from_config


def init_db(config):
    from . import model

    engine = engine_from_config(config.get_settings(), 'sqlalchemy.')
    model.DBSession.configure(bind=engine)
    model.Base.metadata.bind = engine


def includeme(config):
    init_db(config)
