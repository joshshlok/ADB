import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
tf = 0.030

def init():
	gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def reverse():
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True) 
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()

#def forward(tf):
def center():
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, False) 
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()

def right():
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True) 
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()

def left():
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False) 
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()

def stop():
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

	
def key_input(event):
    init()
    print "Key:", event.char
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        reverse(sleep_time)
    elif key_press.lower() == "a":
        left(sleep_time)
    elif key_press.lower() == "d":
        right(sleep_time)
    elif key_press.lower() == "p":
        stop(sleep_time) 
    else:
        pass

#command = tk.Tk()
#command.bind('<KeyPress>', key_input)
#command.mainloop()
