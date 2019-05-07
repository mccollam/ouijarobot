from adafruit_crickit import crickit
import neopixel
import board
from time import sleep

lights = neopixel.NeoPixel(board.A1, 2, brightness=1)

def arm(angle):
	crickit.servo_1.angle = angle

def hand(angle):
	crickit.servo_2.angle = angle

def flash():
	for i in range(5):
		#lights.fill((255,0,255))
		lights[0] = (0, 0, 255)
		lights[1] = (255, 0, 255)
		sleep(.05)
		#lights.fill((255,0,0))
		lights[0] = (255, 0, 0)
		lights[1] = (0, 0, 255)
		sleep(.05)
	lights.fill((255, 0, 0))

def letter(a, h):
	arm(a)
	hand(h)
	sleep(.75)
	flash()

def error():
	arm(90)
	hand(90)
	for i in range(10):
		lights.fill((255, 255, 255))
		sleep(.05)
		lights.fill((0, 0, 0))
		sleep(.05)
	lights.fill((255, 0, 0))

def start():
	hand(90)
	arm(90)
	lights.fill((255,0,0))

### Set up for start
start()
flash()

while True:
	l = input("")
	if l == 'a':
		letter(110, 87)
	elif l == 'b':
		letter(105, 85)
	elif l == 'c':
		letter(100, 84)
	elif l == 'd':
		letter(91, 65)
	elif l == 'e':
		letter(85, 60)
	elif l == 'f':
		letter(80, 56)
	elif l == 'g':
		letter(85, 92)
	elif l == 'h':
		letter(81, 93)
	elif l == 'i':
		letter(69, 56)
	elif l == 'j':
		letter(66, 54)
	elif l == 'k':
		letter(65, 70)
	elif l == 'l':
		letter(68, 95)
	elif l == 'm':
		letter(61, 88)
	elif l == 'n':
		letter(98, 17)
	elif l == 'o':
		letter(92, 12)
	elif l == 'p':
		letter(87, 10)
	elif l == 'q':
		letter(81, 5)
	elif l == 'r':
		letter(76, 4)
	elif l == 's':
		letter(71, 0)
	elif l == 't':
		letter(98, 141)
	elif l == 'u':
		letter(93, 140)
	elif l == 'v':
		letter(88, 138)
	elif l == 'w':
		letter(82, 137)
	elif l == 'x':
		letter(76, 138)
	elif l == 'y':
		letter(72, 132)
	elif l == 'z':
		letter(66, 127)
	elif l == '0':
		letter(117, 163)
	elif l == '1':
		letter(114, 166)
	elif l == '2':
		letter(111, 166)
	elif l == '3':
		letter(108, 166)
	elif l == '4':
		letter(103, 166)
	elif l == '5':
		letter(100, 166)
	elif l == '6':
		letter(95, 166)
	elif l == '7':
		letter(92, 166)
	elif l == '8':
		letter(89, 166)
	elif l == '9':
		letter(85, 166)
	elif l == '(':
		letter(130, 154)
	elif l == ',':
		letter(127, 158)
	elif l == '@':
		letter(124, 158)
	elif l == '!':
		letter(120, 158)
	elif l == '?':
		letter(79, 160)
	elif l == ':':
		letter(76, 160)
	elif l == '.':
		letter(73, 160)
	elif l == ')':
		letter(71, 160)
	else:
		error()
	
	# Let the sender know we received data
	#print(".")
	# Let the buffer clear
	#sleep(.1)
