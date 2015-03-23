$(document).ready( function() {

    $("#up").click( function(event) {
        $.get('/twu/game/move/', {direction: "up"}, function(data){
            $("#game_screen").html(data);
        });
    });

    $("#down").click( function(event) {
        $.get('/twu/game/move/', {direction: "down"}, function(data){
            $("#game_screen").html(data);
        });
    });

    $("#left").click( function(event) {
        $.get('/twu/game/move/', {direction: "left"}, function(data){
            $("#game_screen").html(data);
        });
    });

    $("#right").click( function(event) {
        $.get('/twu/game/move/', {direction: "right"}, function(data){
            $("#game_screen").html(data);
        });
    });

    $("#dice").click( function(event) {
        $.get('/twu/game/roll_dice/', {}, function(data){
            $("#dice").html(data);
        });
    });

    $(".move").click( function(event) {
        $.get('/twu/game/get_score/', {}, function(data){
            $("#score_counter").html(data);
        });
	$.get('/twu/game/character_info/', {}, function(data){
	    $("#leftbar").html(data);
	});
    });



});