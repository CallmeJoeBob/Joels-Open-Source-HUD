# Python application to run Joel's Open Source HUD (Josh)

# Imports
from board import D0, D1
import busio
from display import adafruit_ssd1306
import socket
from datetime import datetime
import asyncio
import time

# Pull fonts
SMALL_FONT = str(__file__.replace('/main.py', '/font5x8.bin'))

# Initialize display
i2c = busio.I2C(D1, D0)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

#Initialize socket server for battery
HOST = "127.0.0.1"
PORT = 8423
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
def clear_display():
  display.fill(0)

# Draw corner borders
def draw_borders():
  display.line(1,50,10,50, 1)
  display.line(1,50,1,60, 1)
  display.line(63,50,53,50, 1)
  display.line(63,50,63,60, 1)
  display.line(1,127,10,127, 1)
  display.line(1,127,1,117, 1)
  display.line(63,127,53,127, 1)
  display.line(63,127,63,117, 1)

# Show battery
def write_battery():
  client.send(('get battery').encode())
  response = client.recv(4096)
  battery_percentage = int(float(str(response).replace('b\'', '').replace('\\n\'', '').replace('battery: ', '')))

  # Battery logo
  display.line(20,119,25,119, 1)
  display.line(20,125,25,125, 1)
  display.line(20,119,20,125, 1)
  display.line(25,119,25,125, 1)
  display.line(22,118,23,118, 1)

  display.text(str(battery_percentage), 30, 119, 1, font_name=SMALL_FONT, wrap=False)

def write_time():
  now = datetime.now()
  current_time = now.strftime("%-I:%M %p")
  display.text(current_time, 10, 53, 1, font_name=SMALL_FONT, wrap=False)

def display_base_screen(loop):
  while True:
    try:
      clear_display()
      draw_borders()
      write_time()
      write_battery()
      display.show()
    except:
      print("Unable to update display.")
    time.sleep(1)


# Start main
loop = asyncio.get_event_loop()

loop.call_soon(display_base_screen, loop)
loop.run_forever()
