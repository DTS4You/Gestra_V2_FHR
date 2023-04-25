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

    module_objects.generate_objects()
    module_objects.init_ddbs()
    module_objects.ddbs_default()
    module_objects.ws2812_defaults()

    print("Init End!")


# -----------------------------------------------------------------------------
def loop_run():
    loop_time = 200             # Loop-Time in (ms)
    i = 0
    while True:
        module_objects.ddbs_default()
        module_objects.ws2812_defaults()
        time.sleep_ms(loop_time)


# =============================================================================
if __name__ == '__main__':

    init_run()
    loop_run()
    print("=== End of Program ===")
# =============================================================================
