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
        
    def show(self, title):
#        page = self.page_q.filter_by(title=title).first()
#        page = find_one_page(title)

        print title
        schedule = DaySchedule(title)

        c.title = schedule.day + " " + str(schedule.date)
        c.content = str(schedule.schedule)
        c.schedule = schedule

        return render('/pages/show.mako')

    @jsonify
    def json(self, title):
        schedule = DaySchedule(title)
        
        result = {}
        result["rows"] = [{"cell": list(row)} for row in schedule.schedule]

        return result

