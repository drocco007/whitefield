<%inherit file="/base.mako"/>\

<%def name="header()">${c.schedule.date_str}\
% if c.schedule.day_type:
&mdash;${c.schedule.day_type}\
%endif
</%def>

<div id="schedule-container">
<p id="previous"><a href="${c.schedule.day_before}">${c.schedule.day_before}</a></p>

% if c.schedule.schedule:
<table id="schedule">
   <tr>
     <th>Time</th>
     <th>Period</th>
   </tr>

   <% flipper = False %> 

   % for timeslot, value in c.schedule.schedule:
   <tr${self.flip_class(flipper)}>
     <% start, end = timeslot.split("-") %>\
     <td>${start}&ndash;${end}</td>
    <td>${value}</td>
   </tr>
   <% flipper = not flipper %>\
   % endfor
</table>
%endif

<p id="next"><a href="${c.schedule.day_after}">${c.schedule.day_after}</a></p>
</div>

<%def name="flip_class(flip)">\
% if flip: 
 class="even"\
% endif
</%def>

