//Instructions at:https://core-electronics.com.au/guides/using-usb-and-bluetooth-controllers-with-python
//If I get errors, it could help to hard restart my Puck.js, connect on Espruino Web IDE, upload (flash) the code, then turn on/off bluetooth on my LAPTOP and reconnect again. 

var kb = require("ble_hid_keyboard");
NRF.setServices(undefined, { hid : kb.report });
var reset_timer;
var next = "b"; //this is the letter that goes to the terminal 

function sendNext(){
  sendCharNext();
  LED2.set();
  setTimeout("LED2.reset()",1000);
}

function sendCharNext(){
        if (next == next.toLowerCase()){
            sk = 0;
        } else {
            sk = 0x02;
        }
        // send the "n" keyboard character
        kb.tap(kb.KEY[next.toUpperCase()], sk);
}

setWatch(function(e) {
  if(e.time-e.lastTime < 0.5){ // on short press slide goes one step forward
    sendNext();
  }
}, BTN, {edge:"falling", debounce:50, repeat:true});

