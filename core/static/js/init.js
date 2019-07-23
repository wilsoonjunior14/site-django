$(document).ready(function(){

	$('.sidenav').sidenav();
	var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
    $('.datepicker').datepicker();
    $('.tooltipped').tooltip();

});