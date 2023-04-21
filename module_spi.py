# #############################################################################
# ### SPI
# ### V 0.10
# #############################################################################
import machine
import time



###############################################################################
# Settings

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(17, machine.Pin.OUT)

# Initialize SPI
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18),
                  mosi=machine.Pin(19),
                  miso=machine.Pin(16))
spi.init()  # bringt keine Änderung


###############################################################################


# Functions

def reg_write(reg, data):
    # Write 1 byte to the specified device and register.

    # Construct message (set ~W bit low, MB bit low)
    msg = bytearray()
    msg.append(0x00)  # 0x00 -> Device OpCode
    msg.append(reg)
    msg.append(data)
    cs.value(0)
    spi.write(msg)
    cs.value(1)


def reg_read(reg, nbytes=1):
    # Read 1 byte from specified register.

    # Construct message
    msg = bytearray()
    msg.append(0x00 | 1)  # 0x00 ->  | write bit
    msg.append(reg)

    # Send out SPI message and read
    cs.value(0)
    spi.write(msg)
    data = spi.read(nbytes)
    cs.value(1)
    return data


###############################################################################
# Main

# Start CS pin high
cs.value(1)


sleeptime = 0.03
# Run forever
while True:

    reg_write(0x00, 0b00000001)
    time.sleep(sleeptime)
