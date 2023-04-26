# #############################################################################
# ### Tracks
# ### V 0.10
# #############################################################################
import defaults


# Bahnen der Schmutzteile
class Track_Seg:

    def __init__(self, ws2812_pio, num_pix, offset=0, direction=False, hit_rb_y=0, hit_rb_z=0):
        """Bahnen der Schmutzteile \n
        num_pix = Anzahl der LEDs \n
        direction = False -> Links nach Rechts \n
        direction = True  -> Rechts nach Links \n
        hit_rb_y = Y-Position (vorne-hinten) der Kollision mit dem Radarstrahl \n
        hit_rb_z = Z-Position (Höhe) der Kollision mit dem Radarstrahl"""
        self.ws2812_pio = ws2812_pio
        self.num_pix = num_pix
        self.offset = offset
        self.direction = direction
        self.hit_rb_y = hit_rb_y
        self.hit_rb_z = hit_rb_z

    def get_direction(self):
        return self.direction


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    my_tracks = []
    for i in range(defaults.Tracks.num_of_tracks):
        my_tracks.append(Track_Seg(defaults.Tracks.num_of_leds,
                                   defaults.Tracks.offset[i],
                                   defaults.Tracks.direction[i],
                                   defaults.Tracks.track_hit_y[i],
                                   defaults.Tracks.track_hit_z[i]))

    print(len(my_tracks))
    for i in range(len(my_tracks)):
        print("Track > ", i, "LEDs->", my_tracks[i].num_pix, "| Offset->", my_tracks[i].offset, "| Dir->", my_tracks[i].direction,
              "| hit_y->", my_tracks[i].hit_rb_y, "| hit_z->", my_tracks[i].hit_rb_z)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
