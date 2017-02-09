$(document).ready(function() {

	$('#ticket-form').on('submit', function(event){
		event.preventDefault();
		console.log("form submitted!")  // sanity check
		create_ticket();
	});

    function form_processed(jsondata) {
        var whitenums = JSON.stringify(jsondata['golden_ticket'][0], null, 2).slice(2, -2).trim()
        var rednum = JSON.stringify(jsondata['golden_ticket'][1], null, 2).slice(2, -2).trim()
        $('.error-alert').remove();
        $('#ticket-form')[0].reset();
        $('#drone-table tr:first').after('<tr><td>' + jsondata['drone_name'] + '</td>' + 
            '<td>[' + JSON.stringify(jsondata['white_vals'], null, 2).slice(2, -2).trim() + ']' +
            '[' + JSON.stringify(jsondata['red_val'], null, 2).trim() + ']</td></tr>');
        $('#golden-ticket').replaceWith('<h4 id="golden-ticket" class="numbers">[' +
            whitenums + ']<span class="powerball">[' + rednum + ']</span></h4>');
    }

    function form_invalid(jsondata) {
        $('.error-alert').remove();
        for(var e in jsondata['error_list']) {
            $("#form-errors").append('<div class="error-alert">'+ jsondata['error_list'][e] +'</div>')
        }
    }

	function create_ticket() {
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
                if(json['status'] === 'success') {
                    form_processed(json)
                } else {
                    form_invalid(json)
                }
            },
			error: function(xhr) {
            	console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			}
		});
	};
});
