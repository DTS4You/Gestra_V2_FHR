# #############################################################################
# ### SPI
# ### V 0.10
# #############################################################################
import machine
import time


class SPI:

    def __init__(self):
        # Assign chip select (CS) pin (and start it high)
        self.cs = machine.Pin(17, machine.Pin.OUT)
        self.cs.value(1)

        # Initialize SPI
        self.spi = machine.SPI(0,
                          baudrate=1000000,
                          polarity=1,
                          phase=1,
                          bits=8,
                          firstbit=machine.SPI.MSB,
                          sck=machine.Pin(18),
                          mosi=machine.Pin(19),
                          miso=machine.Pin(16))
        self.spi.init()
        self.msg = bytearray()
        self.data = [0, 0, 0, 0]

    def reg_write(self, reg, num_of_bytes):
        self.msg = bytearray()
        self.msg.append(reg)
        for i in range(num_of_bytes):
            self.msg.append(self.data[i])
        self.cs.value(0)
        self.spi.write(self.msg)
        self.cs.value(1)

    def ddb_cs(self, value):
        self.cs.value(value)

    def ddb_init(self, num_leds):
        self.data[0] = num_leds
        self.reg_write(0xB1, 1)

    def ddb_show(self):
        self.reg_write(0xB2, 0)

    def ddb_set_rgb(self, r, g, b):
        self.data[0] = r
        self.data[1] = g
        self.data[2] = b
        self.reg_write(0xA1, 3)

    def ddb_show_raw(self):
        self.spi.write(0xB2)

# -----------------------------------------------------------------------------
def main():
    spi = SPI()

    sleeptime = 0.03
    # Run forever
    while True:
        #spi.ddb_cs(0)
        spi.ddb_init(20)
        spi.ddb_set_rgb(20, 20, 20)
        spi.ddb_show()
        #spi.ddb_cs(1)
        time.sleep(sleeptime)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
