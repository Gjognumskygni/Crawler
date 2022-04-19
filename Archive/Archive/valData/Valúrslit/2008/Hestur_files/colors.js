
(function ($) {  

  Drupal.behaviors.bootstrap_subtheme2 = {

    attach: function (context, settings) {            

     // All our js code here

//------------------------------default farvur---------------------//

     //Taxonomy farva á forsíðuni
       $( (window.location.pathname == "/") || (window.location.pathname == "/forsida") || (window.location.pathname == "/forsida/english") ).each(function() {

            //Aktuelt blátt - default
                      $('.views-field-term-node-tid').css("color","rgb(91,191,221)");

            //Mentan reytt
                      $('.views-field-term-node-tid:contains("Mentan")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Átrúnaður")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Bókmentir")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Børn")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Byggilist")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Leiklist")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Myndlist")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Sniðgeving")').css("color","rgb(227,72,30)");
                      $('.views-field-term-node-tid:contains("Tónleikur")').css("color","rgb(227,72,30)");

            //Ítróttur grønt
                      $('.views-field-term-node-tid:contains("Ítróttur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Annar ítróttur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Fimleikur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Flogbóltur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Fótbóltur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Hondbóltur")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Kappróður")').css("color","rgb(96,195,99)");
                      $('.views-field-term-node-tid:contains("Svimjing")').css("color","rgb(96,195,99)");

//-----------------------------------default farvur endar her--------------------//


//------------------------------------Special blocks on frontpage ----------------------//


$(document).ready(function () {
     

var color = $("#news_x3 .views-row-1 .views-field-term-node-tid").css("color");

if( color == 'rgb(96, 195, 99)' ) {


            $('#news_x3 .views-row-1').css({'background':'rgb(96, 195, 99)'});
            $('#news_x3 .views-row-1 .views-field-title').css({'max-width': '186px', 'margin-left': '8px'});
            $('#news_x3 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x3 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x3 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});




        }  else if ( color == 'rgb(227, 72, 30)' ) {
          



            $('#news_x3 .views-row-1').css({'background':'rgb(227, 72, 30)'});
            $('#news_x3 .views-row-1 .views-field-title').css({'max-width': '186px', 'margin-left': '8px'});
            $('#news_x3 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x3 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x3 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});



        } else if ( color == 'rgb(91, 191, 221)' ) {


            $('#news_x3 .views-row-1').css({'background':'rgb(91, 191, 221)'});
            $('#news_x3 .views-row-1 .views-field-title').css({'max-width': '186px', 'margin-left': '8px'});
            $('#news_x3 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x3 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x3 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});


        }

});




$(document).ready(function () {
     

var color = $("#news_x2a .views-row-2 .views-field-term-node-tid").css("color");

if( color == 'rgb(96, 195, 99)' ) {


            $('#news_x2a .views-row-2').css({'background':'rgb(96, 195, 99)'});
            $('#news_x2a .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2a .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2a .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});




        }  else if ( color == 'rgb(227, 72, 30)' ) {
          



            $('#news_x2a .views-row-2').css({'background':'rgb(227, 72, 30)'});
            $('#news_x2a .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2a .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2a .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});



        } else if ( color == 'rgb(91, 191, 221)' ) {


            $('#news_x2a .views-row-2').css({'background':'rgb(91, 191, 221)'});
            $('#news_x2a .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2a .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('#news_x2a .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2a .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});


        }

});


$(document).ready(function () {
     

var color = $(".news_x2b_2 .views-row-1 .views-field-term-node-tid").css("color");

if( color == 'rgb(96, 195, 99)' ) {


            $('.news_x2b_2 .views-row-1').css({'background':'rgb(96, 195, 99)'});
            $('.news_x2b_2 .views-row-1 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('.news_x2b_2 .views-row-1 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('.news_x2b_2 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});




        }  else if ( color == 'rgb(227, 72, 30)' ) {
          



            $('.news_x2b_2 .views-row-1').css({'background':'rgb(227, 72, 30)'});
            $('.news_x2b_2 .views-row-1 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('.news_x2b_2 .views-row-1 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('.news_x2b_2 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});



        } else if ( color == 'rgb(91, 191, 221)' ) {


            $('.news_x2b_2 .views-row-1').css({'background':'rgb(91, 191, 221)'});
            $('.news_x2b_2 .views-row-1 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('.news_x2b_2 .views-row-1 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px'});
            $('.news_x2b_2 .views-row-1 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('.news_x2b_2 .views-row-1 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});



        }

});


$(document).ready(function () {
     

var color = $("#news_x2b .views-row-2 .views-field-term-node-tid").css("color");

if( color == 'rgb(96, 195, 99)' ) {


            $('#news_x2b .views-row-2').css({'background':'rgb(96, 195, 99)'});
            $('#news_x2b .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2b .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2b .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'max-width': '296px'});
            $('#news_x2b .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2b .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});

        }  else if ( color == 'rgb(227, 72, 30)' ) {

            $('#news_x2b .views-row-2').css({'background':'rgb(227, 72, 30)'});
            $('#news_x2b .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2b .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2b .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'max-width': '296px'});
            $('#news_x2b .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2b .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});



        } else if ( color == 'rgb(91, 191, 221)' ) {


            $('#news_x2b .views-row-2').css({'background':'rgb(91, 191, 221)'});
            $('#news_x2b .views-row-2 .views-field-title').css({'max-width': '296px', 'margin-left': '8px'});
            $('#news_x2b .views-row-2 .views-field-title a').css({'color': 'rgb(255, 255, 255)'});
            $('#news_x2b .views-row-2 .views-field-field-summary-article').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'max-width': '296px'});
            $('#news_x2b .views-row-2 .views-field-field-publish').css({'color': 'rgb(255, 255, 255)', 'margin-left': '8px', 'font-weight': 'normal'});
            $('#news_x2b .views-row-2 .views-field-term-node-tid').css({'color': 'rgb(255, 255, 255)', 'font-weight': 'normal'});


        }

});
      

/*--------------------------------------Special blocks on frontpage endar---------------------------*/       

      });


      // All your js code ends here

   }

 };})(jQuery);




