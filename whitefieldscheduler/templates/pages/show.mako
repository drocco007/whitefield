<%inherit file="/base.mako"/>\

<div id="schedule-container">
<p id="previous"><a href="${c.schedule.day_before}">${c.schedule.day_before}</a></p>

<table id="schedule">
<tbody>
    <tr class="top">
        <th colspan="2">
            <span id="date">${c.schedule.short_date_str}</span>
% if c.schedule.day_type:
            <span id="day_code_separator">&mdash;</span>
            <span id="day_code">${c.schedule.day_type}</span>
%endif
            &nbsp;<img src="calendar.gif" /></th>
    </tr>

% if c.schedule.schedule:
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
%endif
</tbody>
</table>

<p id="next"><a href="${c.schedule.day_after}">${c.schedule.day_after}</a></p>

<div id="calendar"></div>
</div>

<%def name="flip_class(flip)">\
% if flip:
 class="even"\
% endif
</%def>
