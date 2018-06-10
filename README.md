# Beagleboard-Robotic-Ship

A robotic ship coded in a beagleboard that uses two HCSR04 sensors to detect obstacles appearing before it and below it. An LED glows as soon as obstacles of appreciable width are detected by the HCSR04 sensors.

## Prerequisites

  - Python 3.6
  - pip install Adafruit-GPIO ( not required if using Raspberry PI or BeagleBoard - already installed )
  
## Finally

   - Connect sensors and LED to appropriate GPIO PINS.
   - Run the script using `python robo_ship.py`
   

![1876-04](https://user-images.githubusercontent.com/27961735/41203647-c3d81ba4-6cf7-11e8-8a0d-e6b08a77221c.jpg)
