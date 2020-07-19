Please go through 
https://github.com/mbechtel2/DeepPicar-v2/wiki/Setup-and-Operation

We changed code 
1. params.py where Drv_L298.py is used as actuator driver
2. Added Drv_L298 is your main code working with wifi 
3. init_kbd.py Removed serial port init() from read_single_keypress
4. picar-mini-kbd-common.py is changed with our actuator driver Drv_L298.py it will take 

For camera you need to study following lib, if opencv does not work. 
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7