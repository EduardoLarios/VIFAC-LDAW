/* global $ */


$('.datepicker').pickadate({

    selectMonths: true, // Creates a dropdown to control month
    selectYears: 50,
    format: 'yyyy-mm-dd',
    max: new Date(),


});
/*
*/
//$(".button-collapse").sideNav();
 $('.collapsible').collapsible();

$('.button-collapse').sideNav({
      menuWidth: 320, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
  );

var $input = $('#fEntrada').pickadate();

// Use the picker object directly.
var picker = $input.pickadate('picker');

picker.set('select', new Date(), { format: 'yyyy-mm-dd' });

    $('select').material_select();
     $('ul.tabs').tabs();


$(document).ready(function() {




$("#Next_Hist_Familiar").click(function(){
    $('ul.tabs').tabs('select_tab', 'Hist_Familiar');  });


      $("#Next_Ocupacion").click(function(){
    $('ul.tabs').tabs('select_tab', 'Ocupacion');  });

     $("#Next_Situacion_Actual").click(function(){
    $('ul.tabs').tabs('select_tab', 'Situacion_Actual'); });

    $("#Next_Archivos").click(function(){
    $('ul.tabs').tabs('select_tab', 'Archivos'); });

     $("#Next_Personal").click(function(){
    $('ul.tabs').tabs('select_tab', 'Personal'); });

      $(window).scroll(function(){
		if ($(this).scrollTop() >= 0) {
			$('.scrollToTop').fadeIn();
		} else {
			$('.scrollToTop').fadeOut();
		}
	});
		$('.scrollToTop').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});


});

$(function() {
    $('#foto').picEdit();
});

$('#foto').picEdit({
    formSubmitted: function(response){
        swal({
          title: "El expediente ha sido guardado con éxito",
          text: "¿Deseas agregar archivos?",
          type: "success",
          showCancelButton: true,
          confirmButtonColor: "#009688",
          confirmButtonText: "Sí, llévame allá",
          cancelButtonText: "No, cancelar",
          closeOnConfirm: false,
          closeOnCancel: false
        },
        function(isConfirm){
          if (isConfirm) {
            swal("¡Perfecto!", "Vamos allá");
            $('ul.tabs').tabs('select_tab', 'Archivos');
          } else {
        	    swal({
                  title: "¿Deseas regresar a la pantalla de inicio?",
                  type: "warning",
                  showCancelButton: true,
                  confirmButtonColor: "#009688",
                  confirmButtonText: "Sí, llévame allá",
                  cancelButtonText: "No, deseo quedarme",
                  closeOnConfirm: false,
                  closeOnCancel: true
                },
                function(isConfirm){
                  if (isConfirm) {
                    document.getElementById("inicio").click();
                  } else {

                  }
                });
          }
        });
    }
});

