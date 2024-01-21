const i2c = require('i2c-bus');
const smallFont = require('oled-font-3x5');
const largeFont = require('oled-font-5x7');
const oled = require('oled-i2c-bus');

const i2cBus = i2c.openSync(0);
const display = new oled(i2cBus, {
    width: 128, // if you have a lower resolution display, replace these
    height: 64,
    address: 0x3c
});

let state = 'idle';

clearScreen();
idle();

function clearScreen() {
    display.stopScroll();
    display.clearDisplay();
}

function idle() {
    drawTime(1, 84, largeFont);
    if (isIdle) {
        setTimeout(idle, 500);
    }
}

function drawTime(x, y, font) {
    var now = new Date();
    var hours = now.getHours(),
        minutes = now.getMinutes(),
        ind = 'AM';
    if (hours > 12) {
        hours = hours - 12;
        ind = 'PM';
    }
    if (minutes < 10) {
        minutes = '0' + minutes;
    }

    display.setCursor(x, y);
    display.writeString(font, 1, hours + ':' + minutes + ' ' + ind, 1, false);
}
