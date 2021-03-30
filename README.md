# UltrasonicSensor RPI with Email Triggering Function 📧

This tutorial will show you guys on how to use the Ultrasonic Sensors (HC-SR04) on Raspberry Pi 4. To make this tutorial more interesting, I have added a simple additional thing which is email triggering function.

The Ultrasonic Sensor will keep tracking the distance until the distance fall below certain level, the alarm will be trigger and send an email to someone with the timestamp and the distance recorded. Other than that, the Raspberry Pi 4 will also save a text file of the distance recorded when the alarm triggered.

The email triggering function will need to user to input the email address and the password ⚠(THIS MIGHT CAUSED SAFETY ISSUES). Anyway, this tutorial is just for testing purposes, Just don't share to others before remove your credentials in the codes.

## The Pin Layout for the Raspberry Pi 4 B+ 📌🤏
<p align="center">
  <img src="https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Header-with-Photo.png" width="600" height="400"/>
</p>

## The Pin Layout for the Ultrasonic Sensor 📌🤏
<p align="center">
  <img src="https://microcontrollerslab.com/wp-content/uploads/2014/12/HC-SR04-Ultrasonic-Sensor-Pinout-diagram-768x546.jpg" width="500" height="350"/>
</p>

The Trigger and Echo Pin will be placed on GPIO7 and GPIO11 accordingly (You may change as your preferences)

```
# Define GPIO Pin location
PIN_TRIGGER = 7
PIN_ECHO = 11
```

The setup has done, you should be able to run the codes without any major error.

You can now try and play with other microcontrollers or add on some new features to make it more interesting. 

Good Luck and Have Fun Coding Whole Day Everyday! ☕

### Try it now! 💥💥💥

