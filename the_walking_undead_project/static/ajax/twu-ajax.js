$(document).ready( function() {

    $("#up").click( function(event) {
        $.get('/twu/game/move/', {direction: "up"}, function(data){
		if (data == "1") {
			location.href = ('/twu/game/gameover/')
		} 
		else {
			$("#game_screen").html(data);
		}
        });
    });
	
    $("#down").click( function(event) {
        $.get('/twu/game/move/', {direction: "down"}, function(data){
		if (data == "1") {
			location.href = ('/twu/game/gameover/')
		} 
		else {
			$("#game_screen").html(data);
		}
        });
    });

    $("#left").click( function(event) {
        $.get('/twu/game/move/', {direction: "left"}, function(data){
		if (data == "1") {
			location.href = ('/twu/game/gameover/')
		} 
		else {
			$("#game_screen").html(data);
		}
        });
    });

    $("#right").click( function(event) {
        $.get('/twu/game/move/', {direction: "right"}, function(data){
		if (data == "1") {
			location.href = ('/twu/game/gameover/')
		} 
		else {
			$("#game_screen").html(data);
		}
        });
    });
	
    $("#dice").click( function(event) {
		var number = 1 + Math.floor(Math.random() * 6);
        $.get('/twu/game/roll_dice/', { roll : number}, function(data){
            $("#dice").html(data);
	});
	$.get('/twu/game/player_attack/', {damage : number}, function(data2){
		if (data2 == "1") {
			location.href = ('/twu/game/gameover/')
		} 
		else {
			$("#text_box").html(data2);
		}
        });

    });


    $(".move").click( function(event) {
	$.get('/twu/game/get_score/', {}, function(data){
	    $("#score_counter").html(data);
	});
	$.get('/twu/game/character_info/', {}, function(data2){
	    $("#left_bar").html(data2);
	});
    });


	$("#newmap").click( function(event) {
		$.get('/twu/game/map_refresh/', {}, function(data){
		location.href = ('/twu/game/')	 
        	});
	});

    $(document).keydown(function(e){ 
	if (e.keyCode == 87) 
		$.get('/twu/game/move/', {direction: "up"}, function(data){ 
			if (data == "1") {
				location.href = ('/twu/game/gameover/')
			}
			else {
				$("#game_screen").html(data);
				$.get('/twu/game/get_score/', {}, function(data){
				    $("#score_counter").html(data);
				});
				$.get('/twu/game/character_info/', {}, function(data2){
				    $("#left_bar").html(data2);
				});
			}
		});
	if (e.keyCode == 65) 
		$.get('/twu/game/move/', {direction: "left"}, function(data){ 
			if (data == "1") {
				location.href = ('/twu/game/gameover/')
			}
			else {
				$("#game_screen").html(data);
				$.get('/twu/game/get_score/', {}, function(data){
				    $("#score_counter").html(data);
				});
				$.get('/twu/game/character_info/', {}, function(data2){
				    $("#left_bar").html(data2);
				});
			}
		});
	if (e.keyCode == 68) 
		$.get('/twu/game/move/', {direction: "right"}, function(data){
			if (data == "1") {
				location.href = ('/twu/game/gameover/')
			}
			else {
				$("#game_screen").html(data);
				$.get('/twu/game/get_score/', {}, function(data){
				    $("#score_counter").html(data);
				});
				$.get('/twu/game/character_info/', {}, function(data2){
				    $("#left_bar").html(data2);
				});
			}
		});
	if (e.keyCode == 83) 
		$.get('/twu/game/move/', {direction: "down"}, function(data){ 
			if (data == "1") {
				location.href = ('/twu/game/gameover/')
			}
			else {
				$("#game_screen").html(data);
				$.get('/twu/game/get_score/', {}, function(data){
				    $("#score_counter").html(data);
				});
				$.get('/twu/game/character_info/', {}, function(data2){
				    $("#left_bar").html(data2);
				});

			}
		});
    });

});