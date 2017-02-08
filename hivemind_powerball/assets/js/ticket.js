$(document).ready(function() {

	$('#ticket-form').on('submit', function(event){
		event.preventDefault();
		console.log("form submitted!")  // sanity check
		create_ticket();
	});

	function create_ticket() {
		console.log("create ticket is working")  // sanity check
		$.ajax({
			type: "POST",
			url: "/ticket/add/",
			data: {
				first_name: $('#id_first_name').val(),
				last_name: $('#id_last_name').val(),
				white1: $('#id_white1').val(),
				white2: $('#id_white2').val(),
				white3: $('#id_white3').val(),
				white4: $('#id_white4').val(),
				white5: $('#id_white5').val(),
				red1: $('#id_red1').val(),
			},
			success: function(json) {
				console.log(json);
				console.log("Success!");
				$('#ticket-form')[0].reset();
                $('#drone-table tr:last').after('<tr><td>' + json['drone_name'] + '</td>' +
                                                    '<td>[' + JSON.stringify(json['white_vals'], null, 2).slice(2, -2).trim() + ']</td>' +
                                                    '<td>' + json['red_val'] + '</td></tr>')
			},
			error: function(xhr) {
            	console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			}
		});
	};
});
