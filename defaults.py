###############################################################################
# MyGlobals
###############################################################################

class DDB:
    num_of_ddbs     = 4


class Stripe:
    num_of_stripes  = 8
    # num_of_pixel    = 79					 # LEDs pro Segment 
    num_of_pixel    = 16					# LEDs === Debug ===
    num_of_leds     = num_of_pixel * 2                      # Kann über die Segmente berechnet werden
    pio_no          = [  0,  1,  2,  3,  4,  5,  6,  7]     # PIO 0-7
    pin_no          = [  2,  3,  4,  5,  6,  7,  8,  9]     # GPIO 2-9


class Radar_Beams:
    num_of_beams    = 4                 # Anzahl Radar Sendestrahlen
    # num_of_leds     = 64              # LEDs in Senderichtung
    num_of_leds     = 12                # LEDs in Senderichtung === Debug ===
    target_hit_x    = 44                # Trefferposition von Links nach Rechts in LEDs gerechnet
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
    num_of_tracks   = 16            # Anzahl der Schrott-Teilbahnen
    # num_of_leds     = 79            # Alle gleich Lang
    num_of_leds     = 16            # Debug !!!
    # PIO Nummer -> Zuweisung LED-Segment zu LED-Stripe
    ws2812_pio      = [  0,         # 0     ->  1.
                         0,         # 1     ->  2.
                         1,         # 2     ->  3.
                         1,         # 3     ->  4.
                         2,         # 4     ->  5.
                         2,         # 5     ->  6.
                         3,         # 6     ->  7.
                         3,         # 7     ->  8.
                         4,         # 8     ->  9.
                         4,         # 9     -> 10.
                         5,         # 10    -> 11.
                         5,         # 11    -> 12.
                         6,         # 12    -> 13.
                         6,         # 13    -> 14.
                         7,         # 14    -> 15.
                         7]         # 15    -> 16.

    offset          = [  0,                 # 0     ->  1.
                         num_of_leds,       # 1     ->  2.
                         0,                 # 2     ->  3.
                         num_of_leds,       # 3     ->  4.
                         0,                 # 4     ->  5.
                         num_of_leds,       # 5     ->  6.
                         0,                 # 6     ->  7.
                         num_of_leds,       # 7     ->  8.
                         0,                 # 8     ->  9.
                         num_of_leds,       # 9     -> 10.
                         0,                 # 10    -> 11.
                         num_of_leds,       # 11    -> 12.
                         0,                 # 12    -> 13.
                         num_of_leds,       # 13    -> 14.
                         0,                 # 14    -> 15.
                         num_of_leds]       # 15    -> 16.

    # Direction -> True = Rechts nach Links -> False = Links nach Rechts
    direction       = [ True,       # 0     ->  1.
                        False,      # 1     ->  2.
                        True,       # 2     ->  3.
                        False,      # 3     ->  4.
                        True,       # 4     ->  5.
                        False,      # 5     ->  6.
                        True,       # 6     ->  7.
                        False,      # 7     ->  8.
                        True,       # 8     ->  9.
                        False,      # 9     -> 10.
                        True,       # 10    -> 11.
                        False,      # 11    -> 12.
                        True,       # 12    -> 13.
                        False,      # 13    -> 14.
                        True,       # 14    -> 15.
                        False]      # 15    -> 16.
    # Gibt die Y-Position (hinten-vorne) an, auf den der Radar-Strahls die Bahn treffen könnte
    track_hit_y     = [  0,         # 0     ->  1.      -> Einspeisung 1
                         1,         # 1     ->  2.
                         2,         # 2     ->  3.      -> Einspeisung 2
                         3,         # 3     ->  4.
                         0,         # 4     ->  5.      -> Einspeisung 3
                         1,         # 5     ->  6.
                         2,         # 6     ->  7.      -> Einspeisung 4
                         3,         # 7     ->  8.
                         0,         # 8     ->  9.      -> Einspeisung 5
                         1,         # 9     -> 10.
                         2,         # 10    -> 11.      -> Einspeisung 6
                         3,         # 11    -> 12.
                         0,         # 12    -> 13.      -> Einspeisung 7
                         1,         # 13    -> 14.
                         2,         # 14    -> 15.      -> Einspeisung 8
                         3]         # 15    -> 16.
    # Gibt die Höhe an, auf der der Rader-Strahl die Bahn treffen könnte
    track_hit_z     = [ 22,         # 0     ->  1.
                        22,         # 1     ->  2.
                        22,         # 2     ->  3.
                        22,         # 3     ->  4.
                        38,         # 4     ->  5.
                        38,         # 5     ->  6.
                        38,         # 6     ->  7.
                        38,         # 7     ->  8.
                        38,         # 8     ->  9.
                        38,         # 9     -> 10.
                        38,         # 10    -> 11.
                        38,         # 11    -> 12.
                        44,         # 12    -> 13.
                        44,         # 13    -> 14.
                        44,         # 14    -> 15.
                        44]         # 15    -> 16.


class Colors:
    default         = [  0,  0,  2]         # Blau 2%
    start           = [  0, 20,  0]         # Grün
    end             = [ 20,  0,  0]         # Rot
    led_on          = [ 50, 50, 50]         # Ein -> weiß
    led_off         = [  0,  0,  0]         # Aus
    target          = [ 50, 20,  0]         # Gelb
    radar_send      = [  0, 50,  0]         # Blau
    radar_receive   = [ 50,  0,  0]         # Rot


class Values:
    loop_time_ms    = 30                    # Loop-Time in (ms)
    loop_time_s     = loop_time_ms / 1000
    wait_cycle_min  = 2                     # Anzahl der min. Radarstrahlenverläufe bis neue Schottteile erzeugt werden
    wait_cycle_max  = 10                    # Anzahl der max. Radarstrahlenverläufe bis neue Schottteile erzeugt werden
    ddb_wait_time   = 5


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
