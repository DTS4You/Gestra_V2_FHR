# #############################################################################
# ### Radar Beams
# ### V 0.10
# #############################################################################
import time

import defaults


class Radar_Beam:

    def __init__(self, num_pix):
        self.num_pix = num_pix
        self.position = 0
        self.hit_flag = False
        self.start_flag = True
        self.end_flag = False
        self.direction = False
        self.led_offset = 0

    def next_position(self):
        if not self.end_flag:
            if not self.direction:      # False = unten nach oben / True = oben nach unten
                self.position += 1
                if self.position >= self.num_pix:
                    self.end_flag = True
            else:
                self.position -= 1
                if self.position < 1:
                    self.end_flag = True
        return self.end_flag

    def get_position(self):
        return self.position

    def get_end_flag(self):
        return self.end_flag

    def get_direction(self):
        return self.direction

    def set_hit(self):
        self.direction = True
        self.hit_flag = True

    def set_new(self):
        self.position = 0
        self.end_flag = False
        self.direction = False
        self.hit_flag = False


class Radar_Reflect:

    def __init__(self, num_pix):
        self.num_pix = num_pix
        self.position = 0
        self.hit_flag = False
        self.start_flag = True
        self.end_flag = False
        self.direction = False


# -----------------------------------------------------------------------------
def main():
    print("Start Global Init")
    my_rb = []
    for i in range(defaults.Radar_Beams.num_of_beams):
        my_rb.append(Radar_Beam(defaults.Radar_Beams.num_of_leds))
    my_rf = []
    for i in range(defaults.Radar_Reflect.num_of_beams):
        my_rf.append(Radar_Reflect(defaults.Radar_Reflect.num_of_leds))

    i = 0
    while i < 200:
        print(my_rb[0].get_position())
        if my_rb[0].get_position() == 8:
            my_rb[0].set_hit()
        if my_rb[0].get_end_flag():
            print("End_Flag")
        my_rb[0].next_position()
        i += 1
        time.sleep(0.3)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================

# Radar Strahlen von Position 0 bis "end_flag"
# Bei Treffer mit Target -> Farbe auf Rot und zurück zur Position 0
