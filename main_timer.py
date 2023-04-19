# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
from machine import Pin, Timer          # importing pin, and timer class

import module_globals


led = Pin(25, Pin.OUT)                   # GPIO14 as led output

led.value(False)                         # LED is off




def timer_init_1(period_ms):        # Timer next Step Radar-Beams
    timer_1 = Timer(-1)
    timer_1.init(period=period_ms, mode=Timer.PERIODIC, callback=toggle_led)
    return timer_1


def timer_init_2(period_ms):
    timer_2 = Timer(-1)
    timer_2.init(period=period_ms, mode=Timer.PERIODIC, callback=time_step)
    return timer_2


def timer_stop_1(timer_1):
    timer_1.deinit()


def timer_stop_2(timer_2):
    timer_2.deinit()


def time_step(timer_2):
    print("Test")


def toggle_led(timer_1):
    led.value(not led.value())


# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")
    t1 = timer_init_1(100)
    t2 = timer_init_2(500)
    try:
        while True:
            print("Wait_Loop")
            time.sleep(1.0)
    except KeyboardInterrupt:
        timer_stop_1(t1)
        timer_stop_2(t2)
        led.value(False)
        print("Main loop ended!")


# =============================================================================
if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")
# =============================================================================
