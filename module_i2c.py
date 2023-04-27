# #############################################################################
# ### I2C
# ### V 0.11
# #############################################################################
from machine import Pin, I2C
from lib.mcp23017 import MCP23017
import time


class GPIO:

    def __init__(self, blink_time=10, run_time= 1000):
        i2c = I2C(0, scl=Pin(21), sda=Pin(20))
        self.mcp = MCP23017(i2c, 0x20)
        self.input = False
        self.output = False
        self.state = False
        self.run_counter = 0
        self.run_time = run_time
        self.blink_state = False
        self.blink_counter = 0
        self.blink_time = blink_time

    def get_input(self, pin):
        self.input = self.mcp.pin(pin, mode=1, pullup=True)
        return self.input

    def set_output(self, pin, state):
        self.mcp.pin(pin, mode=0, value=state)
        return self.output

    def get_button(self):
        if self.state:
            self.blink_counter += 1
            if self.blink_counter > self.blink_time:
                self.blink_state = not self.blink_state
                self.blink_counter = 0
            self.run_counter += 1
            if self.run_counter > self.run_time:
                self.state = False
                self.blink_state = False
                self.blink_counter = 0
                self.run_counter = 0
        else:
            self.state = self.state or self.get_input(8)
        self.set_output(0, not self.blink_state)
        return self.state


# -----------------------------------------------------------------------------
def main():
    gpio = GPIO()

    while True:

        if gpio.get_button():
            print("On")
        time.sleep(0.03)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
