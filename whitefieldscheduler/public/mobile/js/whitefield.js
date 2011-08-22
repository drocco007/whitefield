function date_selected(dateText, datepicker) {
    window.location = "/" + dateText
}

function show_calendar() {
    $("#calendar").datepicker({
		showOn: 'button',
		buttonImage: 'calendar.gif',
		buttonImageOnly: true,
		onSelect: date_selected,
		dateFormat: 'yy-mm-dd',
	});
}

$(document).ready(
    function() {
        $(".top").click(show_calendar);
    }
)
