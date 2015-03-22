$(document).ready( function() {


 
	$("#up").click( function(event) {
           
		   $.get('/twu/game/go_up/', {}, function(event){
            $('#game_screen').html(data);
        });
});

$("#down").click( function(event) {
          
		   $.get('/twu/game/go_down/', {}, function(event){
            $('#game_screen').html(data);
        });
});

$("#left").click( function() {
	$.get('/twu/game/go_left/')
	$('#game_screen').html(data);
    });

    $("#right").click( function() {
	$.get('/twu/game/go_right/')
	$('#game_screen').html(data);
    });
	
	
$.ajax({
  type: "POST",
  url: "~/../pythonBasics/map.py",
  data: { direction: down}
}).done(function( player_move ) {
   // do something
});

});