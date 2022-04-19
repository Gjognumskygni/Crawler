/*
  diverse js til skránna..
  */
  // console.log('skra.js loaded..');
(function ($) {
  $(document).ready(_start);
}(jQuery));
function _start()
{
	//console.log('skra.js loaded.');
	var impath='/sites/all/themes/bootstrap_subtheme/images/skra/';
 	(function ($) {
			var implus='plus.png';
			var imminus='minus.png';
			var sv=$('.page-svskra');
			if(sv.length>0){
				implus='plussv.png';
				imminus='minussv.png';
			}
		// hanga klikk uppá expandaraknøtt á skránni
		$(".s-expand").click(
			function(){
				console.log($(this));
				var p=$(this)[0].parentNode.nextSibling;
				var src=$(this)[0].firstChild.src;
				var x=$(this).parent().parent().next();
				var lin=$(this).parent().next();
				//console.log(implus);
				//console.log(lin);
				//console.log(x);
				if(src.indexOf('plus')>1){
					if(lin.hasClass('s-timer-notimer'))
						lin.delay(200).hide();
					x.slideDown(200);
					$(this)[0].firstChild.src=impath + imminus;
				}else{
					$(this)[0].firstChild.src=impath + implus;
					x.slideUp(200);
					lin.delay(200).fadeIn('fast');
				}
			});
		// justera lista við innsløgum..
		var spot=$('.spot');
		for(var i=0;i<spot.length;i++)
			spot[i].style.display='block';
		// fjerna dupultar myndir, um so er at bæði sending og sendingasíða finst
		var send=$('.s-imgmedia');
		for(var i=0;i<send.length;i++){
			var prev=send[i].previousElementSibling;
			if(prev!=undefined)
				prev.style.display='none';
		}
		// tvinga justering av view-header við margin-top
		//console.log($('.s-pane-block .view-header'));
		//$('.s-pane-block .view-header').css('margin-bottom','-11px');
		//$('.s-pane-block .s-normal-block').css('margin-top','-3px');
		//console.log($('.s-pane-block .s-normal-block'));
		// tvinga fyrsta element aftaná aktuellu sending eitt sindur upp
		var block=$('.s-pane-block .view-content:eq(2)');
	/*	if(block.length>0){
			for(var i=0;i<block.length;i++){
				var cl=block[i].children[0];
				//console.log(cl);
				//console.log('class: ' + cl.style.class);
				//console.log('className:' + cl.style.className);
				//console.log('classes: ' + cl.style.classes);
			}
			//block[0].children[1].style.marginTop="-9px";
		}*/
		// timari til dagføring av tíðarlinju á skránni (NB: tað kann vera meir enn ein!)
		if(_timer==null){
			timer=$('.s-timer-background-block');
			if(timer.length>0){
				_timer = timer;
				window.setTimeout(progress,3000);
			}
		}

		// justering av skrá-navigering (bara á main)
		var navigator=$('.date-prev');
		if(navigator.length>0){
			var imprev='prev.png';
			var imnext='next.png';
			var sv=$('.page-nskra-sv');
			if(sv.length>0){
				imprev='prevsv.png';
				imnext='nextsv.png';
			}
			//console.log(imprev);
			var prev=$(".date-prev")[0].firstElementChild;
			var prevd=prev.search.split('=')[1];
			//console.log(prev);
			prev.innerHTML='<img src="' + impath + imprev +'" />';
			prev.style.backgroundColor='white';
			prev.title="Far til dagin áðrenn henda";
			prev.style.paddingTop='0px';
			var next=$(".date-next")[0].firstElementChild;
			var nn=$(".date-next")[0];
			// text-element við &nbsp; kemur onkustaðnis frá??
			nn.removeChild(nn.firstChild);
			var nextd=next.search.split('=')[1];
			next.innerHTML='<img src="' + impath + imnext + '" />';
			next.style.backgroundColor='white';
			next.title="Far til næsta dag";
			next.style.paddingTop = '0px';
			var d=new Date(prevd);
			d.setDate(d.getDate() + 1);
			var now=new Date();
			now.setHours(0,0,0,0);
			//console.log(d);
			//console.log(now);
			var dag=$(".date-heading h3");
			//console.log(dag);
			var txt=dag[0].innerText + ', ';
			if(d.valueOf()==now.valueOf())
				txt="Í dag, ";
			now.setDate(now.getDate() -1 );
			if(d.valueOf()==now.valueOf())
				txt="Í gjár, ";
			now.setDate(now.getDate()+2);
			if(d.valueOf()==now.valueOf())
				txt="Í morgin, ";
			dag[0].innerText=txt;
		}
	}(jQuery));
/*	$('.s-option').on("click",".s-option",null,
			function(){
				console.log($(this));
			});*/
}

var _timer=null;
function progress(){
	if(_timer==null) return;
//	console.log('tick:' + _timer.length);
	// return;
	var tcnt=0;
	for(var i=0;i<_timer.length;i++){
		var tim=_timer[i];
		var start=tim.getAttribute('data-start');
		var stop = tim.getAttribute('data-stop');
		if(typeof(start)=='undefined'){
			console.log('startundefined');
			return;
		}
		if(start==''){
			console.log('startempty');
			return;
		}
		if(typeof(stop)=='undefined'){
			console.log('stopundefined');
			return;
		}
		if(stop==''){
			console.log('stopempty');
			return;
		}
		var now = Math.floor(Date.now()/1000);
		var len= stop - start;
		var pct= Math.floor(tim.clientWidth * (now - start)/len);
		pct = Math.min(pct,tim.clientWidth-1);
		//console.log('width: ' + tim.clientWidth + ', progress: ' + pct);
		var elem=tim.firstElementChild;
		if(elem==undefined)
			return;
		elem.style.width = pct + 'px';
		if(now>stop){
			//console.log('will reload..');
			//window.setTimeout(reload,10000);
			//..ger onki, bíða eftir at brúkarin ger refresh..
		}else
			tcnt++;
	}
	if(tcnt>0)
       window.setTimeout(progress,3000);

}
/*
function reload(){
	location.reload();
}
*/
