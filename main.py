# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung FHR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import defaults
import module_objects
# import micropython
# import machine


# -----------------------------------------------------------------------------
def init_run():

    print("Init Run")

    module_objects.generate_objects()           # Objekte anlegen
    module_objects.ddbs_init()                  # Digi-Dot-Booster Module initalisieren
    module_objects.ddbs_default()               # Vorgabewerte ausgeben
    module_objects.ws2812_defaults()            # WS2812-PIO Einheiten initalisieren

    print("Init End!")


# -----------------------------------------------------------------------------
def loop_run():

    i = 0
    while True:
        module_objects.ddbs_default()
        module_objects.ws2812_defaults()
        time.sleep_ms(defaults.Values.loop_time_ms)


# =============================================================================
if __name__ == '__main__':

    init_run()
    loop_run()
    print("=== End of Program ===")
# =============================================================================
