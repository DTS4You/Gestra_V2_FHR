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

    def reg_write(self, reg, data):
        # Write 1 byte to the specified device and register.

        # Construct message (set ~W bit low, MB bit low)
        self.msg = bytearray()
        self.msg.append(0x00)  # 0x00 -> Device OpCode
        self.msg.append(reg)
        self.msg.append(data)
        self.cs.value(0)
        self.spi.write(self.msg)
        self.cs.value(1)


# -----------------------------------------------------------------------------
def main():
    spi = SPI()

    sleeptime = 0.03
    # Run forever
    while True:
        spi.reg_write(0x00, 0b00000001)
        time.sleep(sleeptime)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
