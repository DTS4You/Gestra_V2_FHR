# #############################################################################
# ### Digi-Dot-Booster -> SPI
# ### V 0.11
# ### CS_0 - 3 -> GPIO 10 - 13
# #############################################################################
import machine
import time

import defaults


class SPI:

    def __init__(self):
        # Assign chip select (CS) pin (and start it high)
        self.cs = []
        self.cs.append(machine.Pin(10, machine.Pin.OUT))
        self.cs.append(machine.Pin(11, machine.Pin.OUT))
        self.cs.append(machine.Pin(12, machine.Pin.OUT))
        self.cs.append(machine.Pin(13, machine.Pin.OUT))
        self.cs[0].value(1)
        self.cs[1].value(1)
        self.cs[2].value(1)
        self.cs[3].value(1)

        # Initialize SPI
        self.spi = machine.SPI(0,
                               baudrate=1000000,
                               polarity=0,
                               phase=0,
                               bits=8,
                               firstbit=machine.SPI.MSB,
                               sck=machine.Pin(18),
                               mosi=machine.Pin(19),
                               miso=machine.Pin(16))
        self.spi.init()
        self.ddb_num = 0  # 0-3 -> DigiDot-Booster Modul
        self.msg = bytearray()
        self.data = [0, 0, 0, 0]

    def reg_write(self, reg, num_of_bytes):
        self.msg = bytearray()
        self.msg.append(reg)
        for i in range(num_of_bytes):
            self.msg.append(self.data[i])
        self.cs[self.ddb_num].value(0)
        self.spi.write(self.msg)
        self.cs[self.ddb_num].value(1)

    def ddb_cs(self, value):
        self.cs[self.ddb_num].value(value)

    def ddb_init(self, ddb, num_leds):
        self.ddb_num = ddb
        self.data[0] = num_leds
        self.data[1] = 24
        self.reg_write(0xB1, 2)
        time.sleep_ms(20)

    def ddb_show(self, ddb):
        self.ddb_num = ddb
        self.reg_write(0xB2, 0)

    def ddb_show_all(self):                         # Alle Digi-Dot-Booster -> Show
        for i in range(defaults.DDB.num_of_ddbs):
            self.ddb_show(i)

    def ddb_set_rgb(self, ddb, r, g, b):
        self.ddb_num = ddb
        self.data[0] = r
        self.data[1] = g
        self.data[2] = b
        self.reg_write(0xA1, 3)

    def ddb_set_color(self, ddb, color):            # !!! New
        self.ddb_num = ddb
        self.data[0] = color[0]
        self.data[1] = color[1]
        self.data[2] = color[2]
        self.reg_write(0xA1, 3)

    def ddb_set_led(self, ddb, num):
        self.ddb_num = ddb
        self.data[0] = num
        self.reg_write(0xA4, 1)

    def ddb_set_all(self, ddb):
        self.ddb_num = ddb
        self.reg_write(0xA5, 0)

    def ddb_show_raw(self):
        self.spi.write(0xB2)


# -----------------------------------------------------------------------------
def main():
    spi = SPI()

    sleeptime = 30

    for i in range(4):
        spi.ddb_init(i, 20)
    for i in range(4):
        spi.ddb_init(i, 20)

    i = 0
    # Run forever
    while True:
        # spi.ddb_cs(0)
        for ddb in range(4):
            spi.ddb_set_rgb(ddb, 0, 0, 0)
            spi.ddb_set_all(ddb)
            time.sleep_us(700)
            if i < 20:
                spi.ddb_set_rgb(ddb, 0, 0, 50)
                spi.ddb_set_led(ddb, 20 - i - 1)
            else:
                i = 0

        for ddb in range(4):
            spi.ddb_show(ddb)

        i += 1
        time.sleep_ms(sleeptime)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================

