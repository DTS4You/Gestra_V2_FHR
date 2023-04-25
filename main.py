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


# -----------------------------------------------------------------------------
def init_run():

    print("Init Run")

    module_objects.generate_objects()           # Objekte anlegen
    module_objects.ddbs_init()                  # Digi-Dot-Booster Module initalisieren
    module_objects.ddbs_default()               # Vorgabewerte ausgeben
    module_objects.ws2812_defaults()            # WS2812-PIO Einheiten initalisieren
    module_objects.gpio_set_output(0)           # Taster LED aus
    button = module_i2c.Button()

    print("Init End!")


# -----------------------------------------------------------------------------
def loop_run():

    i = 0
    j = 0
    while True:
        if i > 2:
            print(module_objects.gpio_get_input())
            i = 0
        module_objects.ddbs_default()
        if j > 10:
            module_objects.ws2812_defaults()
            j = 0
        i += 1
        j += 1
        time.sleep_ms(defaults.Values.loop_time_ms)


# =============================================================================
if __name__ == '__main__':

    init_run()
    loop_run()
    print("=== End of Program ===")
# =============================================================================
