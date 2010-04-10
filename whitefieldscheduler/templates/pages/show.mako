<%inherit file="/base.mako"/>\

<div id="schedule-container">
<p id="previous"><a href="${c.schedule.day_before}">${c.schedule.day_before}</a></p>

<table id="schedule">
<tbody>
    <tr class="top">
        <th colspan="2">${c.schedule.short_date_str}\
% if c.schedule.day_type:
&mdash;${c.schedule.day_type}\
%endif
</th>
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
</div>

<%def name="flip_class(flip)">\
% if flip: 
 class="even"\
% endif
</%def>

