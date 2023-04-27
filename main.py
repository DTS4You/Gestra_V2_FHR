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

# global button
# global state_logic, tracks, targets, radar_beams, radar_reflects, ddb, stripe, gpio


# -----------------------------------------------------------------------------
def init_run():

    global button

    print("Init Run")

    module_objects.generate_objects()           # Objekte anlegen
    module_objects.ddbs_init()                  # Digi-Dot-Booster Module init
    module_objects.ws2812_init()                # WS2812 init
    module_objects.ddbs_default_all()           # Vorgabewerte ausgeben
    module_objects.ddbs_show_all()
    module_objects.ws2812_defaults_all()        # Vorgabewerte ausgeben
    module_objects.ws2812_show_all()
    time.sleep(1)
    module_objects.ddbs_start_stop()
    module_objects.ws2812_start_stop()
    time.sleep(2)
    module_objects.ddbs_default_all()           # Vorgabewerte ausgeben
    module_objects.ddbs_show_all()
    module_objects.ws2812_defaults_all()
    module_objects.ws2812_show_all()
    button = module_i2c.GPIO(30, 8000)          # BlinkRate , Dauer

    print("Init End!")


# -----------------------------------------------------------------------------
def loop_run():

    i = 0
    while True:

        if button.get_button():
            module_objects.logic_next_step()
        else:
            module_objects.logic_reset()
            module_objects.ddbs_default_all()
            module_objects.ddbs_show_all()
            if i > 20:
                module_objects.ws2812_defaults_all()
                module_objects.ws2812_show_all()
                i = 0
            i += 1
        time.sleep_ms(defaults.Values.loop_time_ms)


# =============================================================================
if __name__ == '__main__':

    init_run()
    loop_run()
    print("=== End of Program ===")
# =============================================================================
