/*
  diverse jquery ting
  standard decoration av elementum .. navigatión, standard yvirskrift..
  15-02-2017, kpo

  */

var stdpath1='/sites/all/themes/bootstrap_subtheme/images/skra/';
var stdpath2='/sites/all/themes/bootstrap_subtheme/images/';

var _playms=stdpath1 + 'ms.png';
var _plusuv=stdpath1 + 'plus.png';
var _minusuv=stdpath1 + 'minus.png';
var _plussv = stdpath1 + 'plussv.png';
var _minussv = stdpath1 + 'minussv.png';
var _playuv = stdpath1 + 'listento.png';
var _playsv = stdpath1 + 'playsv.png';
var _prevuv = stdpath1 + 'prev.png';
var _prevsv = stdpath1 + 'prevsv.png';
var _nextuv = stdpath1 + 'next.png';
var _nextsv= stdpath1 + 'nextsv.png';
var _playsmalluv = stdpath1 + 'playsmall.png';
var _playsmallsv = stdpath1 + 'playsmallsv.png';
var _clock = stdpath1 + 'clock.png';
var _arrow = stdpath2 + 'arrow.png';


var _links=Array(
//    'href="javascript:function(){return undefined;}" onclick="window.open(' + "'/popout/widget','name','height=250,width=710'" +');"',
	'href="javascript:popoutuv();"',
	'href="/live/1"',
	'href="/nskra/uv"',
	'href="/nskra/sv"',
	'href="/sendingar/uv"',
	'href="/sendingar/sv"',
	'href="/sendingar/eldriuv',
	'href="/sendingar/eldrisv',
	'href="javascript:popoutting();"',
	'href="/live/tingvarp"'
	);

function popoutting() {
    window.open("/webservice/player/tingradio.php", "_blank", "toolbar=no, scrollbars=no, resizable=yes, top=0, left=0, width=400, height=40");
}
function popoutuv(){
	window.open('/popout/widget','name','height=250,width=710');
}



(function ($) {
	Drupal.behaviors.buildOverlay78 = {
    attach: function (context, settings) {
			_start();


function _start()
{
	//console.log('kvf_decorator loaded.');
 	(function ($) {
		var man = $(".manual-li");
		//console.log(man);
		for(var i=0;i<man.length;i++){
			var at = man[i].innerHTML;
			var s="";
			//console.log(at);
			switch(at){
				case 'liveuv':
					s=bld(_links[0],'Beinleiðis útvarp',_playuv);
					break;
				case 'livesv':
					s=bld(_links[1],'Beinleiðis sjónvarp',_playsv);
					break;
				case 'skrauv':
					s=bld(_links[2],'Skráin - útvarp',_arrow);
					break;
				case 'skrasv':
					s=bld(_links[3],'Skráin - sjónvarp',_arrow);
					break;
				case 'sendinguv':
					s=bld(_links[4],'Sendingar - útvarp',_arrow);
					break;
				case 'sendingsv':
					s=bld(_links[5],'Sendingar - sjónvarp',_arrow);
					break;
				case 'eldriuv':
					s=bld(_links[6],'Eldri sendingar - útvarp',_arrow);
					break;
				case 'eldrisv':
					s=bld(_links[7],'Eldri sendingar - sjónvarp',_arrow);
					break;
				case 'tinguv':
					s=bld(_links[8],'Tingvarp útvarp',_playuv);
					break;
				case 'tingsv':
					s=bld(_links[9],'Tingvarp sjónvarp',_playsv);
					break;
				default:
				    s="";
					var t=man[i].firstElementChild;
					if(t.nodeName=='A'){
						var tx=t.innerHTML;
						var im=_arrow;
						t.innerHTML='<div class="caption">' + tx + '</div><div class="option"><img src="' + _arrow + '" /></div>';
					}
					//console.log('default');
					//console.log(t);
			}
			if(s!="")
				man[i].innerHTML = s;
		}
		// tvinga linkar upp á pláss.. dunno hví hetta er neyðugt
		var header=$('.s-headerlink a');
		//console.log(header);
		for(var i=0;i<header.length;i++){
			header[i].style.color='white';
		}
		$('.newest-media img').width('91px');

		var over=$("div[data-type]");
		for(var i=0;i<over.length;i++){
			var t=over[i].getAttribute('data-type');
			var l=over[i].getAttribute('data-longd');
			if(t=='Media - Audio' || t=='Media - Video'){
				var lnk = over[i].firstElementChild;
				//console.log(lnk.nodeName);
				if(lnk!=undefined){
					im = lnk.firstElementChild;
					if(im!=undefined && im.nodeName=='IMG'){
						lnk.innerHTML = buildOverlay(lnk,t,l);
					}
				}
			}

			if(t=='Media - Myndasavn'){
	      var lnk = over[i].firstElementChild;
	      //console.log(lnk.nodeName);
	      if(lnk!=undefined){
	        im = lnk.firstElementChild;
	        if(im!=undefined && im.nodeName=='IMG'){
	          lnk.innerHTML = buildOverlay2(lnk,t);
	        }
	      }
	    }

		}

	}(jQuery));
}
function bld(lnk,cap,img)
{
	return '<a ' + lnk + '><div class="caption">' + cap + '</div><div class="option"><img src="' + img + '" /></div></a>';
}
function buildOverlay(lnk,ty,len){
  var s=lnk.innerHTML;
  var play=_playsv;
  if(ty=='Media - Audio')
	  play=_playuv;
  var sec= parseInt(len,10);
  var date=new Date(null);
  date.setSeconds(sec);
  //console.log(date.toISOString());
  if(sec<3600)
	  len=date.toISOString().substr(14,5);
  else
	  len=date.toISOString().substr(11,8);
  var ret= s + '<div style="position:relative;top:-16px">';
  ret +='<div style="position:absolute;background-color:#212121;color:white;font-size:10px;padding:1px">';
  ret +='<img src="' + play + '" style="float:left;margin-left:2px;margin-right:4px"/>';
  ret +='<span style="margin-right:4px">' + len + '</span></div></div>';
  return ret;
}
function buildOverlay2(lnk,ty){
  var s=lnk.innerHTML;
  var play=_playms;
  //console.log(_playms);
  var ret2= s + '<div style="position:relative;top:-18px">';
  ret2 +='<div style="position:absolute;background-color:#212121;color:white;font-size:10px;padding:2px">';
  ret2 +='<img src="' + play + '" style="float:left;margin-left:2px;margin-right:2px;height:14px;width:14px;"/>';
  //ret +='<span style="margin-right:4px">' + len + '</span></div></div>';
  return ret2;
}



		}
	};
}(jQuery));
