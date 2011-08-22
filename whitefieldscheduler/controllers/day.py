import logging

from cgi import escape

from pylons import request, response, session, tmpl_context as c
from pylons.decorators import jsonify

#from pylons.controllers.util import abort, redirect_to

from whitefieldscheduler.lib.base import BaseController, render

from whitefieldscheduler.model.schedule import DaySchedule

log = logging.getLogger(__name__)

class DayController(BaseController):

#    def __before__(self):
#        self.page_q = Session.query(Page)
        
    def show(self, title, school):
#        page = self.page_q.filter_by(title=title).first()
#        page = find_one_page(title)

        if 'date' in request.params:
            title = request.params['date']

        print title, school
        schedule = DaySchedule(title, school)

        c.title = schedule.day + " " + str(schedule.date)
        c.content = str(schedule.schedule)
        c.schedule = schedule
        c.schedules = [
            DaySchedule(str(schedule.day_before), school),
            schedule,
            DaySchedule(str(schedule.day_after), school),
        ]

        return render('/pages/show.mako')

    def show_mobile(self, title):
        if 'date' in request.params:
            title = request.params['date']

        print "mobile: ", title
        schedule = DaySchedule(title)

        c.title = schedule.day + " " + str(schedule.date)
        c.content = str(schedule.schedule)
        c.schedule = schedule

        return render('/pages/show_mobile.mako')

    @jsonify
    def json(self, title):
        schedule = DaySchedule(title)
        
        result = {}
        result["rows"] = [{"cell": list(row)} for row in schedule.schedule]

        return result

