from machine import Pin
from machine import I2C

# Initialisierung I2C
i2c = I2C(0, sda=Pin(20), scl=Pin(21))

# I2C-Bus-Scan ausgeben
print(i2c.scan())
