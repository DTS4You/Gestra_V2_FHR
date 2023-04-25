# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import defaults

loop_time = 0.5

color = ( 0, 10, 0)


class Colors:
    default         = (  0,  0,  5)
    start           = (  0, 20,  0)
    end             = ( 20,  0,  0)
    led_on          = ( 50, 50, 50)
    led_off         = (  0,  0,  0)
    target          = ( 10, 20, 30)
    radar_send      = ( 10, 20, 30)
    radar_receive   = ( 10, 20, 30)


def set_pixel_ws2812(led_pio, pos, my_color=defaults.Colors.default):
    r, g, b = my_color
    lr = my_color[0]
    lg = my_color[1]
    lb = my_color[2]
    print(my_color, " -> ", r, g, b, " -> ", lr, lg, lb, " -> ", len(my_color))


# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")

    my_color = Colors()

    i = 0

    while i < 100:
        set_pixel_ws2812(0, 0, my_color.start)
        time.sleep(loop_time)
        i += 1


# =============================================================================
if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")
# =============================================================================