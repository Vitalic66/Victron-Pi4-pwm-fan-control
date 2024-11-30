This python is to control a 3 pin fan on a Pi4 running VenusOS from Victron Energy.

The original file / post is public available here:

https://forums.raspberrypi.com/viewtopic.php?t=354125

The fan is controlled via PWM signal from GPIO 14.

Installing RPi.GPIO is needed to be done, to make this python work. 

The filesystem also has to be writeable. 

Do the installation at your own risk. I'm not responsible for any damages by setting up the necessary things wrong.


Installation of RPi.GPIO:

open a ssh terminal session to the Pi4 running VenusOS and enter:

  opkg update
  
  opkg install python3-dev
  
  opkg install packagegroup-core-buildessential
  
  opkg install pip3
  
  pip3 install RPi.GPIO
  

Edit the temperatures in the pwm_fan_control.py to your needs.

It's recommended to test the script in the opened terminal session.

If it works, put it in a crontab, e.g. 

  @reboot python3 /data/pwm_fan_control.py > /dev/null 2>&1

This will start the script at every reboot.

After a firmware update the installation has to be repeated.
