# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *


# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def loser(strip, wait_ms=20):
	for j in range(32):
		strip.setPixelColorRGB(0, 255,255,0)
		strip.setPixelColorRGB(1, 255,255,0)
		strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0) 
		strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0) 
		strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
		strip.show()
		time.sleep(0.05)
		strip.setPixelColorRGB(6, 255,255,0)
                strip.setPixelColorRGB(7, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.05)
	for q in range(8):
		strip.setPixelColorRGB(6, 255,0,0)
                strip.setPixelColorRGB(7, 255,0,0)
                strip.setPixelColorRGB(2, 255,0,0)
                strip.setPixelColorRGB(3, 255,0,0)
                strip.setPixelColorRGB(4, 255,0,0)
                strip.setPixelColorRGB(5, 255,0,0)
                strip.setPixelColorRGB(0, 255,0,0)
                strip.setPixelColorRGB(1, 255,0,0)
                strip.show()
                time.sleep(0.3)
		strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,0,0)
                strip.setPixelColorRGB(4, 0,0,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.3)
def winner(strip, wait_ms=20):
        for j in range(32):
                strip.setPixelColorRGB(0, 255,255,0)
                strip.setPixelColorRGB(1, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.show()
                time.sleep(0.05)
                strip.setPixelColorRGB(6, 255,255,0)
                strip.setPixelColorRGB(7, 255,255,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,8*j,0)
                strip.setPixelColorRGB(4, 0,8*j,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.05)
        for q in range(30):
                strip.setPixelColorRGB(6, 0,255,0)
                strip.setPixelColorRGB(7, 0,255,0)
                strip.setPixelColorRGB(2, 0,255,0)
                strip.setPixelColorRGB(3, 0,255,0)
                strip.setPixelColorRGB(4, 0,255,0)
                strip.setPixelColorRGB(5, 0,255,0)
                strip.setPixelColorRGB(0, 0,255,0)
                strip.setPixelColorRGB(1, 0,255,0)
                strip.show()
                time.sleep(0.1)
                strip.setPixelColorRGB(6, 0,0,0)
                strip.setPixelColorRGB(7, 0,0,0)
                strip.setPixelColorRGB(2, 0,0,0)
                strip.setPixelColorRGB(3, 0,0,0)
                strip.setPixelColorRGB(4, 0,0,0)
                strip.setPixelColorRGB(5, 0,0,0)
                strip.setPixelColorRGB(0, 0,0,0)
                strip.setPixelColorRGB(1, 0,0,0)
                strip.show()
                time.sleep(0.1)

def dispBlock(strip,block, wait_ms=20):
	for j in range(1,2):
		for q in range(7):
			r = int(block[j+0+(6*q)]+block[j+1+(6*q)],16)
			g = int(block[j+2+(6*q)]+block[j+3+(6*q)],16)
			b = int(block[j+4+(6*q)]+block[j+5+(6*q)],16)
			strip.setPixelColorRGB(q, r,g,b)
	strip.show()
	time.sleep(3)



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		block = 'cbaafc80a80fde241a037b87aa69f4615d31e6336520520d504ceef4cd31800d' 
		block = block[1:]
		dispBlock(strip, block)
		loser(strip)
		time.sleep(5)
		winner(strip)
		#print ('Color wipe animations.')
		#colorWipe(strip, Color(255, 0, 0))  # Red wipe
		#colorWipe(strip, Color(0, 255, 0))  # Blue wipe
		#colorWipe(strip, Color(0, 0, 255))  # Green wipe
		#print ('Theater chase animations.')
		#theaterChase(strip, Color(127, 127, 127))  # White theater chase
		#theaterChase(strip, Color(127,   0,   0))  # Red theater chase
		#theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
		#print ('Rainbow animations.')
		#rainbow(strip)
		#rainbowCycle(strip)
		#theaterChaseRainbow(strip)
