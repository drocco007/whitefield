<%inherit file="/mobile_base.mako"/>\

<div id="schedule-container" data-role="page">
    <div data-role="content">
        <h3 id="logo"><span id="w">W</span>hitefield <span id="mobile">Mobile</span></h3>
        <ul data-role="listview" data-inset="true">
            <li id="scheduleDate" data-role="list-divider" data-icon="grid" data-theme="b">
                <a href="#datePage" data-rel="dialog" data-transition="slidedown">

                <span>${c.schedule.short_date_str}</span>
                % if c.schedule.day_type:
                    <span id="day_code_separator">&mdash;</span>
                    <span id="day_code">${c.schedule.day_type}</span>
                %endif

                </a>
            </li>

            % if c.schedule.schedule:
            % for timeslot, value in c.schedule.schedule:
                <li>
                    <div class="ui-grid-a">
                        <div class="ui-block-a">
                            % if timeslot:
                                <% start, end = timeslot.split("-") %>\
                                <strong>${start}&ndash;${end}</strong>
                            % else:
                                &nbsp;
                            % endif
                        </div>
                        <div class="ui-block-b">${value}</div>
                    </div>
                </li>
            % endfor
            %endif
        </ul>
    </div>
</div>

<div id="datePage" data-role="page">
    <div data-role="content">
        <form method="post" action="#">
            <div data-role="fieldcontain">
                <label for="datef">Date Input:</label>
                <input type="date" name="datef" id="datef" value=""  />
            </div>
        </form>
    </div>
</div>

<script>
    $('body').bind('swipeup', function(){
        var date = location.hash.substring(1) || 'today';
        var next = Date.parse(date).add({days: 7});

         $.mobile.changePage(next.toString('yyyy-MM-dd'), 'slideup');
    });

    $('body').bind('swipedown', function(){
        var date = location.hash.substring(1) || 'today';
        var next = Date.parse(date).add({days: -7});
         $.mobile.changePage(next.toString('yyyy-MM-dd'), 'slidedown');
    });

    $('body').bind('swiperight', function(){
        var date = location.hash.substring(1) || 'today';
        var next = Date.parse(date).add({days: -1});

         $.mobile.changePage(next.toString('yyyy-MM-dd'), 'slide', true);
    });

    $('body').bind('swipeleft', function(){
        var date = location.hash.substring(1) || 'today';
        var next = Date.parse(date).add({days: 1});

         $.mobile.changePage(next.toString('yyyy-MM-dd'), 'slide');
    });

    //bind to pagecreate to automatically enhance date inputs
        $( ".ui-page" ).live( "pagecreate", function(){
                $( "input[type='date'], input:jqmData(type='date')", this ).each(function(){
                        $(this).after( $( "<div />" ).datepicker({ altField: "#" + $(this).attr( "id" ), showOtherMonths: true,
                onSelect: function(dateText, instance) {
                    var next = Date.parse(dateText);
                    $.mobile.changePage(next.toString('yyyy-MM-dd'));
                }
            }) );
                });
        });
</script>
