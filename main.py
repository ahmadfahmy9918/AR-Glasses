import Adafruit_SSD1309
import numpy as np
import sounddevice as sd
from bluetooth import *
import pyglet
import select
import board
import busio

# Search for nearby devices
nearby_devices = discover_devices()

# Print the list of nearby devices
for bdaddr in nearby_devices:
    print(bluetooth.lookup_name(bdaddr), bdaddr)

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import pyglet

# Create a window
window = pyglet.window.Window()

# Create a label
label = pyglet.text.Label("Hello, World!",
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')

# Draw the label on the screen
@window.event
def on_draw():
    window.clear()
    label.draw()

# Run the application
pyglet.app.run()

# Create a blank image
image = Image.new('1', (128, 32))

# Draw the text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', 16)
draw.text((0, 0), 'Hello, World!', font=font, fill=1)

# Create an SSD1309 instance
disp = Adafruit_SSD1309.SSD1309_128_32(rst=None)

# Clear the display
disp.clear()
disp.display()

# Display the image on the screen
disp.image(image)
disp.display()


import pyglet
import Adafruit_SSD1309
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Create a blank image
image = Image.new('1', (128, 32))

# Draw the text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', 16)
draw.text((0, 0), 'Hello, World!', font=font, fill=1)

# Create an SSD1309 instance
disp = Adafruit_SSD1309.SSD1309_128_32(rst=None)

# Clear the display
disp.clear()
disp.display()

# Display the image on the screen
disp.image(image)
disp.display()

# Create a window
window = pyglet.window.Window()

# Draw the label on the screen
@window.event
def on_draw():
    window.clear()
    pyglet.image.ImageData(128, 32, 'L', image.tobytes()).blit(0, 0)

# Run the application
pyglet.app.run()


# Create a blank image
image = Image.new('1', (128, 32))

# Draw the text on the image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', 16)
draw.text((0, 0), 'Hello, World!', font=font, fill=1)

# Create an SSD1309 instance
i2c = busio.I2C(board.SCL, board.SDA)
disp = Adafruit_SSD1309.SSD1309_I2C(128, 32, i2c)

# Clear the display
disp.fill(0)
disp.show()

# Display the image on the screen
disp.image(image)
disp.show()

# Create a window
window = pyglet.window.Window()

# Draw the label on the screen
@window.event
def on_draw():
    window.clear()
    pyglet.image.ImageData(128, 32, 'L', image.tobytes()).blit(0, 0)

# Run the application
pyglet.app.run()


