$('body').countdown('2017/01/01', function(event) {
	var offset = event.offset;
	$('#cday').text(offset.totalDays);
	$('#chours').text(''.concat(offset.hours < 10 ? '0' : '', offset.hours));
	$('#cminutes').text(''.concat(offset.minutes < 10 ? '0' : '', offset.minutes));
	$('#cseconds').text(''.concat(offset.seconds < 10 ? '0' : '', offset.seconds));
});

$(document).ready(function(){
	$(".loader").fadeOut(2000);
});