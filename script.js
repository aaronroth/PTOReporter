/*
 Copyright (c) 2013 Aaron Roth
 See the file LICENSE for copying permission.
*/

$(document).ready(function() {	
	$('#from').datepicker({
		defaultDate: '+1w',
		changeMonth: true,
		numberOfMonths: 3,
		onClose: function(selectedDate) {
			$('#to').datepicker('option', 'minDate', selectedDate);
		}
	});
	
	$('#to').datepicker({
		defaultDate: '+1w',
		changeMonth: true,
		numberOfMonths: 3,
		onClose: function(selectedDate) {
			$('from').datepicker('option', 'maxDate', selectedDate);
		}	
	});
	
	$('#content').validate({
		rules: {
			dept: 'required',
			from: {
				required: true,
				date: true
			},
			hours: {
				required: true,
				number: true
			},
			name: 'required',
			sender: {
				required: true,
				email: true
			},
			to: {
				required: true,
				date: true
			},
			type: 'required'
		},
		messages: {
			dept: {
				required: ''
			},
			from: {
				required: '',
				date: ''
			},
			hours: {
				required: '',
				number: ''
			},
			name: {
				required: ''
			},
			sender: {
				required: '',
				email: ''
			},
			to: {
				required: '',
				date: ''
			},
			type: {
				required: ''
			}
		}
	});
});