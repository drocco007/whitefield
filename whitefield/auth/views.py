from pyramid.view import view_config
from .model import User, DBSession


@view_config(route_name='login', renderer='json')
def login(request):
    try:
        user = User.by_email(request.params['email'], DBSession)
        assert user.check_password(request.params['password'])
        return "YOU LOGGED IN!"
    except:
        pass


@view_config(route_name='update_user', renderer='json')
def update_user(request):
    user = User(full_name=request.params['full_name'],
                email=request.params['email'],
                school=request.params['school'])

    user.set_password(request.params['password'])

    DBSession.add(user)

    return {}
