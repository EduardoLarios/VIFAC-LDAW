// Initialize collapse button
  $(".btn-floating").sideNav();
  // Initialize collapsible (uncomment the line below if you use the dropdown variation)
  //$('.collapsible').collapsible();

//Initialize datepicker
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 250 // Creates a dropdown of years to control year
  });

//Initialize comboBox(select)
$(document).ready(function() {
    $('select').material_select();
    $('.collapsible').collapsible();
});

