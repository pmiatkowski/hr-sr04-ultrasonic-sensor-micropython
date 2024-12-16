"""
HR-SR04 Ultrasonic Sensor Class for MicroPython

Author: Pawel Miatkowski
Date: 2024-12-15
License: MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from machine import Pin
import utime

class HRSR04:
    def __init__(self, triggerPin, echoPin):
        self.triggerPin = Pin(triggerPin, Pin.OUT)
        self.echoPin = Pin(echoPin, Pin.IN)
        self.distanceThreshold = 2
        self.previousDistance = None

    def _isInThreshold(self, prevValue, nextValue):
        hi = prevValue + self.distanceThreshold
        low = prevValue - self.distanceThreshold

        if nextValue < hi and nextValue > low:
            return True
        
        return False
    
    def _measureTime(self):
        timepassed = 0
        self.triggerPin.low()
        utime.sleep_us(2)

        self.triggerPin.high()
        utime.sleep_us(10)

        signalon = 0
        signaloff = 0
        
        while self.echoPin.value() == 0:
            signaloff = utime.ticks_us()
        while self.echoPin.value() == 1:
            signalon = utime.ticks_us()

        timepassed = signalon - signaloff

        return timepassed

    # Returns actual distance
    def ping(self):
        time = self._measureTime()
        distanceCM = (time * 0.0343) / 2
        distanceCM = round(distanceCM, 2)
        
        return distanceCM
    
    # Returns difference betwen next and previous distance
    def diffDistance(self):
        nextDistance = self.ping()

        if self.previousDistance == None:
            self.previousDistance = nextDistance

        hasDistanceChanged = not self._isInThreshold(self.previousDistance, nextDistance)
        if hasDistanceChanged:
            diff = nextDistance - self.previousDistance
            self.previousDistance = nextDistance

            return diff
        
        return 0
