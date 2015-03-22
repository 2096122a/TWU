$(document).ready( function() {

    $("#up").click( function() {
	$.get('/twu/game/go_up/', {}, function(data){
            
        });
    });

    $("#down").click( function() {
	$.get('/twu/game/go_down/')
    });

    $("#left").click( function() {
	$.get('/twu/game/go_left/')
    });

    $("#right").click( function() {
	$.get('/twu/game/go_right/')
    });

    $("#up").hover( function() {
            $(this).css('width', 30%);
            $(this).css('height', 12%);
            $( this ).fadeOut( 100 );
    },
    function() {
            $(this).css('width', 25%);
            $(this).css('height', 10%);
            $( this ).fadeIn( 500 );
    });

    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

});
