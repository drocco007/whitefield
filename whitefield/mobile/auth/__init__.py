from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from whitefield.auth import init_db


def init_auth(config):
    authn_policy = AuthTktAuthenticationPolicy(
        '712ef82b1b4541f18225363eb576f585', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_root_factory('whitefield.auth.model.RootFactory')


def init_routes(config):
    config.add_route('login', '/login', request_method='POST')
    config.add_route('logout', '/logout')
    config.add_route('user_info', '/users/current')
    config.add_route('update_user', '/users', request_method='POST')

    config.scan('whitefield.mobile.auth.views')


def includeme(config):
    init_db(config)
    init_auth(config)
    init_routes(config)
