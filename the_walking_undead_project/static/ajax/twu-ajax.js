$(document).ready( function() {

    $("#up").click( function() {
	$.get('/twu/go_up/')
    });

    $("#down").click( function() {
	$.get('/twu/go_down/')
    });

    $("#left").click( function() {
	$.get('/twu/go_left/')
    });

    $("#right").click( function() {
	$.get('/twu/go_right/')
    });


});
