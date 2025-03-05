"""
dht22 sensor = the white one.
gpio 4
"""

import Adafruit_DHT
import time

# Set sensor type
DHT_SENSOR = Adafruit_DHT.DHT22

# Set GPIO pin (using BCM numbering)
DHT_PIN = 4  # Change if using a different GPIO pin

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(2)  # Read every 2 seconds
