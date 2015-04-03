from sqlalchemy import engine_from_config
from . import user


def init_db(config):
    from . import model

    engine = engine_from_config(config.get_settings(), 'sqlalchemy.')
    model.DBSession.configure(bind=engine)
    model.Base.metadata.bind = engine
