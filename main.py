# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import defaults
import module_radar


# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")

    rb_1 = module_radar.Radar_Beam(defaults.Radar.num_of_leds)

    try:
        while True:
            print("Do_Loop")
            print(rb_1)
            time.sleep(defaults.Values.loop_time)
    except KeyboardInterrupt:
        print("Main loop ended!")


# =============================================================================
if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")
# =============================================================================
