# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Blink example for boards with ONLY a NeoPixel LED (e.g. without a built-in red LED).
Includes QT Py and various Trinkeys.
Requires two libraries from the Adafruit CircuitPython Library Bundle.
Download the bundle from circuitpython.org/libraries and copy the
following files to your CIRCUITPY/lib folder:
* neopixel.mpy
* adafruit_pixelbuf.mpy
Once the libraries are copied, save this file as code.py to your CIRCUITPY
drive to run it.
"""
import time
import board
import neopixel

# Specify the number of NeoPixels you have
num_pixels = 3

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the NeoPixels, and the number of NeoPixels to access.  Returns a 
# list 'pixels' of indexable NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels)

while True:
    for i in range(num_pixels):
        pixels[i] = (255, 0, 0)
    time.sleep(0.5)
    
    pixels.fill((0, 0, 0))
    time.sleep(0.5)
