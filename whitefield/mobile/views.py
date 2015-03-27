from pyramid.view import view_config

from whitefield.schedule.views import json_schedule


@view_config(route_name='schedule', renderer='json')
@view_config(route_name='schedule:date', renderer='json')
def schedule(request):
    date_string = request.matchdict.get('date', 'today')
    school = request.params.get('school')
    return json_schedule(date_string, school=school)
