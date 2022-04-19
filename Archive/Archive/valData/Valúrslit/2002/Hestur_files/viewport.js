

(function ($) {  

  Drupal.behaviors.bootstrap_subtheme = {

    attach: function (context, settings) {            

     // All our js code here

     

    if (screen.width > 767 ) {  
        $('head').append('<meta name="viewport" content="width=1024, maximum-scale=1.0, user-scalable=0">');                
    }

    // End

   }

 };})(jQuery);
