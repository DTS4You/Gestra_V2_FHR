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
def main_run():

    print("Main Run")

    try:
        module_objects.generate_objects()
        # print(micropython.mem_info())
        # print(machine.freq())
    except KeyboardInterrupt:
        print("Main loop ended!")


# =============================================================================
if __name__ == '__main__':

    main_run()
    print("=== End of Program ===")
# =============================================================================
