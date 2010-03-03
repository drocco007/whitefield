<%inherit file="/base.mako"/>\

<%def name="header()">${c.title}&mdash;${c.schedule.day_type}</%def>

<table id="schedule">
   <tr>
     <th>Time</th>
     <th>Period</th>
   </tr>

   <% flipper = False %> 

   % for timeslot, value in c.schedule.schedule:
   <tr ${self.flip_class(flipper)}>
     <% start, end = timeslot.split("-") %>

     <td>${start}&ndash;${end}</td>
     <td>${value}</td>
   </tr>

   <% flipper = not flipper %>
   % endfor
</table>

<%def name="flip_class(flip) ">\
  % if flip: 
    class="even"\
  % endif
</%def>

