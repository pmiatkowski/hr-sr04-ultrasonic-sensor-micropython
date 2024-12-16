# HR-SR04 Ultrasonic Sensor Class for MicroPython

Raspberry Pi Pico MicroPython controller for the HR-SR04 ultrasonic sensor. It measures distance in centimeters (cm) and calculates the difference between consecutive readings.

## Usage

The `HRSR04` class needs to be instantiated with two arguments: the trigger pin number and the echo pin number.

```python
TRIGGER_PIN = 0
ECHO_PIN = 1
sensor = HRSR04(TRIGGER_PIN, ECHO_PIN)
```

### Distance reading

Use `sensor.ping()` to get the current distance.

### Distance difference

`sensor.diffDistance()` returns the difference in distance between the previous and current reading. This can be used to determine if an object is approaching or receding.

```pyton
while True:
    check = sensor.diffDistance()
    
    if check < 0:
        print('Is approaching', sensor.ping())
    if check > 0:
        print('Is receding', sensor.ping())
    else:
        pass
    
    utime.sleep_ms(200)
```
