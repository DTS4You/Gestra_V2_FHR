###############################################################################
# MyGlobals
###############################################################################

class DDB:
    num_of_ddbs     = 4


class Stripe:
    num_of_stripes  = 8
    num_of_leds     = 79 * 2                                # Kann über die Segmente berechnet werden
    pio_no          = [  0,  1,  2,  3,  4,  5,  6,  7]     # PIO 0-7
    pin_no          = [  2,  3,  4,  5,  6,  7,  8,  9]     # GPIO 2-9


class Radar_Beams:
    num_of_beams    = 4
    # num_of_leds     = 79              # LEDs in Senderichtung
    num_of_leds     = 12                # LEDs in Senderichtung === Debug ===
    target_hit_pos  = 60                # Trefferposition von Links nach Rechts in LEDs gerechnet
    ddb             = [ 0, 1, 2, 3]


class Radar_Reflect:
    num_of_beams    = 16
#    num_of_leds     = [ 33,             # _0 ->  1. LED-Stripe
#                        31,             # _1 ->  2. LED-Stripe
#                        51,             # _2 ->  3. LED-Stripe
#                        48,             # _3 ->  4. LED-Stripe
#                        33,             # _4 ->  5. LED-Stripe
#                        31,             # _5 ->  6. LED-Stripe
#                        51,             # _6 ->  7. LED-Stripe
#                        48,             # _7 ->  8. LED-Stripe
#                        44,             # _8 ->  9. LED-Stripe
#                        42,             # _9 -> 10. LED-Stripe
#                        46,             # 10 -> 11. LED-Stripe
#                        44,             # 11 -> 12. LED-Stripe
#                        44,             # 12 -> 13. LED-Stripe
#                        42,             # 13 -> 14. LED-Stripe
#                        46,             # 14 -> 15. LED-Stripe
#                        44]             # 15 -> 16. LED-Stripe
    num_of_leds     = [ 4,             # _0 ->  1. LED-Stripe
                        4,             # _1 ->  2. LED-Stripe
                        4,             # _2 ->  3. LED-Stripe
                        4,             # _3 ->  4. LED-Stripe
                        4,             # _4 ->  5. LED-Stripe
                        4,             # _5 ->  6. LED-Stripe
                        4,             # _6 ->  7. LED-Stripe
                        4,             # _7 ->  8. LED-Stripe
                        4,             # _8 ->  9. LED-Stripe
                        4,             # _9 -> 10. LED-Stripe
                        4,             # 10 -> 11. LED-Stripe
                        4,             # 11 -> 12. LED-Stripe
                        4,             # 12 -> 13. LED-Stripe
                        4,             # 13 -> 14. LED-Stripe
                        4,             # 14 -> 15. LED-Stripe
                        4]             # 15 -> 16. LED-Stripe
    num_of_ddb      = [ 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

    direction       = [ True,           # 0
                        False,          # 1
                        True,           # 2
                        False,          # 3
                        True,           # 4
                        False,          # 5
                        True,           # 6
                        False,          # 7
                        True,           # 8
                        False,          # 9
                        True,           # 10
                        False,          # 11
                        True,           # 12
                        False,          # 13
                        True,           # 14
                        False]          # 15


class Target:
    num_of_targets = 10


class Tracks:
    num_of_tracks   = 24
    num_of_leds     = 79
    # PIO Nummer -> Zuweisung LED-Segment zu LED-Stripe
    ws2812_pio      = [  0,         # 1
                         0,         # 2
                         0,         # 3
                         1,         # 4
                         1,         # 5
                         1,         # 6
                         2,         # 7
                         2,         # 8
                         2,         # 9
                         3,         # 10
                         3,         # 11
                         3,         # 12
                         4,         # 13
                         4,         # 14
                         4,         # 15
                         5,         # 16
                         5,         # 17
                         5,         # 18
                         6,         # 19
                         6,         # 20
                         6,         # 21
                         7,         # 22
                         7,         # 23
                         7]         # 24
    # Direction -> True = Rechts nach Links -> False = Links nach Rechts
    direction       = [ True,       # 1
                        False,      # 2
                        False,      # 3
                        False,      # 4
                        False,      # 5
                        False,      # 6
                        False,      # 6
                        False,      # 7
                        False,      # 8
                        False,      # 9
                        False,      # 10
                        False,      # 11
                        False,      # 12
                        False,      # 13
                        False,      # 14
                        False,      # 15
                        False,      # 16
                        False,      # 17
                        False,      # 18
                        False,      # 19
                        False,      # 20
                        False,      # 21
                        False,      # 22
                        False,      # 23
                        False]      # 24
    # Gibt die seitliche Position an, auf den der Radar-Strahls die Bahn treffen könnte
    track_hit_x     = [  0,         # 1
                         1,         # 2
                         2,         # 3
                         3,         # 4
                         0,         # 5
                         0,         # 6
                         0,         # 7
                         0,         # 8
                         0,         # 9
                         0,         # 10
                         0,         # 11
                         0,         # 12
                         0,         # 13
                         0,         # 14
                         0,         # 15
                         0,         # 16
                         0,         # 17
                         0,         # 18
                         0,         # 19
                         0,         # 20
                         0,         # 21
                         0,         # 22
                         0,         # 23
                         0]         # 24
    # Gibt die Höhe an, auf der der Rader-Strahl die Bahn treffen könnte
    track_hit_y     = [ 20,         # 1
                        20,         # 2
                        20,         # 3
                        20,         # 4
                        20,         # 5
                        20,         # 6
                        20,         # 7
                        20,         # 8
                        20,         # 9
                        20,         # 10
                        20,         # 11
                        20,         # 12
                        20,         # 13
                        20,         # 14
                        20,         # 15
                        20,         # 16
                        20,         # 17
                        20,         # 18
                        20,         # 19
                        20,         # 20
                        20,         # 21
                        20,         # 22
                        20,         # 23
                        20]         # 24


class Colors:
    default         = [  0,  0,  5]
    start           = [  0, 20,  0]
    end             = [ 20,  0,  0]
    target          = [ 10, 20, 30]
    radar_send      = [ 10, 20, 30]
    radar_receive   = [ 10, 20, 30]


class Values:
    loop_time       = 0.3
    wait_cycle_min  = 2                  # Anzahl der min. Radarstrahlenverläufe bis neue Schottteile erzeugt werden
    wait_cycle_max  = 10                 # Anzahl der max. Radarstrahlenverläufe bis neue Schottteile erzeugt werden


# -----------------------------------------------------------------------------
def main_task():
    print(Tracks.num_of_tracks)
    print(Colors.target[1])
    print(Colors.radar_send)


# =============================================================================
if __name__ == '__main__':

    main_task()
    print("=== End of Program ===")
# =============================================================================
