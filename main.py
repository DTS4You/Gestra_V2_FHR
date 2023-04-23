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

    module_objects.generate_objects()
    module_objects.init_ddbs()
    module_objects.ddbs_default()

    print("Main loop end!")


# =============================================================================
if __name__ == '__main__':

    main_run()
    print("=== End of Program ===")
# =============================================================================
