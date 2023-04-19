###############################################################################
# MyGlobals
###############################################################################

class Stripe:
    num_of_stripes  = 8
    num_of_leds     = 240                                  # Kann über die Segmente berechnet werden
    pin_no          = [  0,  1,  2,  3,  4,  5,  6,  7]
    pio_no          = [  0,  1,  2,  3,  4,  5,  6,  7]


class Radar:
    num_of_beams    = 4
    # num_of_leds     = 78              # LEDs in Senderichtung
    num_of_leds     = 12                # LEDs in Senderichtung === Debug ===
    target_hit_pos  = 60                # Trefferposition von Links nach Rechts in LEDs gerechnet


class Target:
    num_of_targets = 10


class Tracks:
    num_of_tracks   = 24
    num_of_leds     = 78
    ws2812_pio      =
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
