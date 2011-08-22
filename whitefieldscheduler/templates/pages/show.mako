<%inherit file="/base.mako"/>\

<%
def flip_generator(start=0):
    l = ['even', 'odd']
    count = start

    while True:
        count += 1
        yield l[count % 2]
%>


<div id="schedule-container">
<div id="previous"><a href="${c.schedule.day_before}">${c.schedule.day_before}</a></div>

% for schedule in c.schedules:
<table id="schedule">
<tbody>
    <tr class="top">
        <th colspan="2"><span id="date">${schedule.short_date_str}</span></th>
    </tr>
    <tr class="top">
        <th colspan="2">
% if schedule.day_type:
            <span id="day_code">${schedule.day_type}</span>
%endif
        </th>
    </tr>

    % if schedule.schedule:
       <% flipper = flip_generator() %>
       % for timeslot, value in schedule.schedule:
       <tr class="${flipper.next()}">
         % if timeslot:
         <% start, end = timeslot.split("-") %>\
         <td>${start}&ndash;${end}</td>
         % else:
         <td>&nbsp;</td>
         % endif
         <td>${value}</td>
       </tr>
       % endfor
    % else:
       <tr><td colspan="2">&nbsp;</td></tr>
    % endif
</tbody>
</table>
%endfor

<div id="next"><a href="${c.schedule.day_after}">${c.schedule.day_after}</a></div>

</div>
