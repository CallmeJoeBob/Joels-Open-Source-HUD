# Python application to run Joel's Open Source HUD (Josh)

# Import the pins for i2c bus 0
from board import D0, D1
import busio
from display import adafruit_ssd1306
import socket

# Initialize display
i2c = busio.I2C(D1, D0)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

#Initialize socket server for battery
host = "127.0.0.1"
port = 8423
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
def clear_display():
  display.fill(0)
  display.show()

# Show battery
def write_battery():
  client.send(('get battery').encode())
  response = client.recv(4096)
  display.text(str(response), 0, 0, 1, wrap=True)
  display.show()

# Start main
clear_display()
write_battery()
display.show()
