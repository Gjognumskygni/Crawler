(function ($) {  

  Drupal.behaviors.bootstrap_subtheme3 = {

    attach: function (context, settings) {            



$(window.location.pathname == "/leita").each(function() {



  // All our js code here

  	
  $('.views-widget-sort-order').css("display", "none");

  $('.views-submit-button').insertBefore('.views-widget-filter-type');
  
  
  var input = $('.views-widget .form-type-radio .control-label:first input');
  
  $(".views-widget .form-type-radio .control-label:first").html(' ');
  $(".views-widget .form-type-radio .control-label:first").append(input);
  
  $(".views-widget .form-type-radio .control-label:first").append("Alt");
  
  $('.view-header').insertAfter('.view-filters');

  // All your js code ends here
  
 

      });



   }

 };})(jQuery);