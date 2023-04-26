# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung FHR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import defaults
import module_objects
import module_i2c
# import micropython
# import machine

global button
# global state_logic, tracks, targets, radar_beams, radar_reflects, ddb, stripe, gpio


# -----------------------------------------------------------------------------
def init_run():

    global button

    print("Init Run")

    module_objects.generate_objects()           # Objekte anlegen
    module_objects.ddbs_init()                  # Digi-Dot-Booster Module initalisieren
    module_objects.ddbs_default()               # Vorgabewerte ausgeben
    module_objects.ws2812_defaults()            # WS2812-PIO Einheiten initalisieren
    time.sleep(1)
    module_objects.ddbs_start_stop()
    time.sleep(2)
    module_objects.ddbs_default()               # Vorgabewerte ausgeben
    button = module_i2c.GPIO(5, 100)

    print("Init End!")


# -----------------------------------------------------------------------------
def loop_run():

    i = 0
    while True:

        if button.get_button():
            module_objects.ddbs_start_stop()
            if i > 10:
                module_objects.ws2812_defaults()
                i = 0
            i += 1
        else:
            module_objects.ddbs_default()
            if i > 10:
                module_objects.ws2812_defaults()
                i = 0
            i += 1
        time.sleep_ms(defaults.Values.loop_time_ms)


# =============================================================================
if __name__ == '__main__':

    init_run()
    loop_run()
    print("=== End of Program ===")
# =============================================================================
