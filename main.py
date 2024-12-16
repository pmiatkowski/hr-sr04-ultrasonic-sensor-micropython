from machine import Pin
from hr_sr04 import HRSR04
import utime

pin = Pin("LED", Pin.OUT)
pin.toggle()

# Create an instance of the class with the trigger pin and echo pin.
TRIGGER_PIN = 0
ECHO_PIN = 1
sensor = HRSR04(TRIGGER_PIN, ECHO_PIN)

# Adjust the distance threshold when using the diffDistance method to improve readings.
# The optimal threshold may depend on the environment in which the sensor is used.
# If there are more obstacles, you may need to increase this number.
sensor.distanceThreshold = 3

while True:
    try:
        check = sensor.diffDistance()
        
        if check < 0:
            print('Is approaching', sensor.ping())
        if check > 0:
            print('Is receding', sensor.ping())
        else:
            pass
        # A small delay combined with the distanceThreshold improves diffDistance readings.
        utime.sleep_ms(200)
    except KeyboardInterrupt:
        break


pin.off()
print('The end')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    