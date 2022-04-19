// Audio player
var jwConfigAudio = {
	width:		"100%",
	height:		"42",
	autostart:	false,
	mute:		false,
	controls:	true,
	displaydescription: false,
	displaytitle:   false,
	ga: {                           // Enable Google Analytics
//	  idstring:     'title'
	},
	cast: {                         // Chromecast
	  appid:        '35152BC5'
	},
	floating: {
		dismissible: true
	}
}


// Video player
var jwConfigVideo = {
	aspectratio:	"16:9",
	width:		"100%",
	autostart:	false,
	controls:	true,
	displaydescription: false,
	displaytitle:   false,
	ga: {                           // Enable Google Analytics
//	  idstring:     'title'
	},
	cast: {                         // Chromecast
	  appid:        'AB0072B5'
	},
	sharing: {
	    heading: "Deil",
	    sites: [
		"facebook",
		"twitter",
		"email"
	    ]
	},
	floating: {
		dismissible: true
	},
	playbackRateControls: false,
        "skin": {
         //       "name": "kvf"
        },
}



/***** JW uppsetingar til CK editor plugin *****/
var jwConfigCK = {
	width:		"100%",
	aspectratio:	"16:9",
	autostart:	false,
	image:		"/sites/all/themes/felags/images/logo_on_black.png",
	type: 		'hls',
	events: {
//		onReady: function () { this.play(); this.pause(); }
		onBeforePlay: function () { console.log("fired"); }

	}
}
// Audio player
var jwConfigCKAudio = {
	width:		"100%",
	height:		"40",
	type: 		'hls'
}
