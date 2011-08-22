$(document).ready(function() {
    var date_selected = function(dateText, datepicker) {
        $("#searchForm").submit();
    };

    $("#date").datepicker({
        showOn: 'button',
        buttonImage: '/calendar.gif',
        buttonImageOnly: true,
        onSelect: date_selected,
        dateFormat: 'yy-mm-dd',
        showAnim: "slideDown",
        showOtherMonths: true,
	    selectOtherMonths: true,
        constrainInput: false
    });
});

