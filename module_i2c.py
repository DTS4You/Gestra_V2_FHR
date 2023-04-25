# #############################################################################
# ### I2C
# ### V 0.11
# #############################################################################
from machine import Pin, I2C
from lib.mcp23017 import MCP23017
import time


class GPIO:

    def __init__(self):
        i2c = I2C(0, scl=Pin(21), sda=Pin(20))
        self.mcp = MCP23017(i2c, 0x20)
        self.input = False
        self.output = False

    def get_input(self, pin):
        self.input = self.mcp.pin(pin, mode=1, pullup=True)
        return self.input

    def set_output(self, pin, state):
        self.mcp.pin(pin, mode=0, value=state)
        return self.output


class Button():
    def __init__(self):
        self.state = False
        self.blink_counter = 0



# -----------------------------------------------------------------------------
def main():
    gpio = GPIO()
    
    while True:
        gpio.set_output(0, 0)
        time.sleep(0.3)
        gpio.set_output(0, 1)
        time.sleep(0.3)
        print(gpio.get_input(8))


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
