function init() {
    var SPEED = 64
    var TURN_SPEED_RATIO = 0.5
    var ROT_SPEED = 64

    var button;
    var brakep = 0;

    WebIOPi.prototype.createSlider = function(id, macro, name, min, max, step, value) {
	var div = $('<div></div>');
	// var htmlslider = '<input type="range" min="' + min  + '" max="' + max + '" step="' + step '">'
	var htmlslider = '<input type="range" min="'+min+'" max="'+max+'" step="'+step+'">'
	var slider = $(htmlslider);
	var label = $('<label></label>');

	slider.attr("id", id);
	slider.attr("value", value);
	slider.bind("change", function() {
            webiopi().callMacro(macro, slider.val());
	    label.text(name + ' (' + slider.val() + '):');
	});
	label.attr("for", id);
	label.text(name + ' (' + value + '):');
	div.append(label.add(slider));

	return div;
    }

    function brake() {
	// brakep = brakep ? 0 : 1;
	// $('#bt_brake').toggleClass("btON");
	// webiopi().callMacro("brake", brakep);
	webiopi().callMacro("stop");
    }
    
    function checkbrake() {
	if (brakep)
	    brake();
    }

    function go_f1() {
	checkbrake();
	webiopi().callMacro("go_fl");
    }

    function go_f() {
	checkbrake();
	webiopi().callMacro("go_f");
    }

    function go_fr() {
	checkbrake();
	webiopi().callMacro("go_fr");
    }

    function go_l() {
	checkbrake();
	webiopi().callMacro("go_l");
    }
    
    function go_r() {
	checkbrake();
	webiopi().callMacro("go_r");
    }

    function go_bl() {
	checkbrake();
	webiopi().callMacro("go_bl");
    }

    function go_b() {
	checkbrake();
	webiopi().callMacro("go_b");
    }

    function go_br() {
	checkbrake();
	webiopi().callMacro("go_br");
    }

    function stop() {
	// webiopi().callMacro("stop");
    }

    $("#up").append(webiopi().createButton("bt_fl", "↖", go_f1, stop));
    $("#up").append(webiopi().createButton("bt_f", "↑", go_f, stop));
    $("#up").append(webiopi().createButton("bt_fr", "↗", go_fr, stop));
    $("#middle").append(webiopi().createButton("bt_l", "←", go_l, stop));
    $("#middle").append(webiopi().createButton("bt_brake", "B", brake));
    $("#middle").append(webiopi().createButton("bt_r", "→", go_r, stop));
    $("#down").append(webiopi().createButton("bt_bl", "↙", go_bl, stop));
    $("#down").append(webiopi().createButton("bt_b", "↓", go_b, stop));
    $("#down").append(webiopi().createButton("bt_br", "↘", go_br, stop));
    $("#sliders").append(webiopi().createSlider("s1", "speed", "Speed ", 0, 127, 1, SPEED));
    $("#sliders").append(webiopi().createSlider("s2", "turnRatio", "Turn ratio", 0, 1, 0.01, TURN_SPEED_RATIO));
    $("#sliders").append(webiopi().createSlider("s3", "rotSpeed", "Roation Speed",0, 127, 1, ROT_SPEED));


    // var down = [];
    // var func = null;

    // $(document).keydown(function(e) {
    // 	down[e.keyCode] = true;
    // 	if (func != go_f && down[38]) {
    // 	    func = go_f;
    // 	    go_f();
    // 	}
    // }).keyup(function(e) {
    // 	down[e.keyCode] = false;
    // 	if (e.keyCode == '38') {
    // 	    func = null;
    // 	    stop();
    // 	}
    // });
    
    webiopi().callMacro("stop");
    webiopi().callMacro("speed", SPEED);
    webiopi().callMacro("turnRatio", TURN_SPEED_RATIO);
    webiopi().callMacro("rotSpeed", ROT_SPEED);

    window.onbeforeunload = function(){
	webiopi().callMacro("stop");
    }
    
    window.onunload = function(){
	webiopi().callMacro("stop");
    }

}
webiopi().ready(init);

