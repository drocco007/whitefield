from pyramid.view import view_config

from whitefield.schedule.views import json_schedule


@view_config(route_name='root', renderer='json')
@view_config(route_name='schedule', renderer='json')
@view_config(route_name='schedule:date', renderer='json')
def hello_world(request):
    date_string = request.matchdict.get('date', 'today')
    return json_schedule(date_string)
