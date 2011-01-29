<%inherit file="/base.mako"/>\

<div id="schedule-container">
<div id="previous"><a href="${c.schedule.day_before}"><img src="images/navleft.png" alt="${c.schedule.day_before}" /></a></div>

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
     % if timeslot:
     <% start, end = timeslot.split("-") %>\
     <td>${start}&ndash;${end}</td>
     % else:
     <td>&nbsp;</td>
     % endif
     <td>${value}</td>
   </tr>
   <% flipper = not flipper %>\
   % endfor
%endif
</tbody>
</table>

<div id="next"><a href="${c.schedule.day_after}"><img src="images/navright.png" alt="${c.schedule.day_after}" /></a></div>

<div id="calendar"></div>

</div>

<%def name="flip_class(flip)">\
% if flip:
 class="even"\
% endif
</%def>
