from pyramid.response import Response
from pyramid.security import remember, forget, Authenticated
from pyramid.view import view_config

from whitefield import auth
from whitefield.mobile.views import schedule as anonymous_schedule
from whitefield.auth.model import User, DBSession


@view_config(route_name='login', renderer='json')
def login(request):
    try:
        user = User.by_email(request.params['email'], DBSession)
        assert user.check_password(request.params['password'])
        headers = remember(request, user.id)
        return Response("YOU LOGGED IN!", headers=headers)
    except:
        pass


@view_config(route_name='logout', renderer='json')
def logout(request):
    headers = forget(request)
    return Response("Signed out", headers=headers)


@view_config(route_name='user_info', renderer='json')
def user_info(request):
    try:
        user = User.by_id(request.authenticated_userid, DBSession)
        return auth.user.as_json(user)
    except AttributeError:
        return {}


@view_config(route_name='update_user', renderer='json')
def update_user(request):
    user = User(full_name=request.params['full_name'],
                email=request.params['email'],
                school=request.params['school'])

    user.set_password(request.params['password'])

    DBSession.add(user)

    return {}


@view_config(route_name='schedule', renderer='json',
             effective_principals=Authenticated)
@view_config(route_name='schedule:date', renderer='json',
             effective_principals=Authenticated)
def user_schedule(request):
    schedule = anonymous_schedule(request)
    user = User.by_id(request.authenticated_userid, DBSession)

    schedule['user'] = auth.user.as_json(user)

    return schedule
