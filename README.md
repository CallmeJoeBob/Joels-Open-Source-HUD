# Joels-Open-Source-HUD

### Install:
1. Clone this repo. Make sure you have Node.js installed!
2. Install the dependencies using `npm install websocket i2c-bus oled-i2c-bus oled-font-3x5 oled-font-5x7`
3. Copy the `oled.js` file into `./node_modules/oled-i2c-bus/`. This will replace the file in the module with the swapped x and y coordinates.
4. Run `node main.js` to start the program. Be sure to have the SSD1306 display plugged into the correct I<sup>2</sup>C bus and GPIO pins, and configure the file accordingly!