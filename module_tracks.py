# #############################################################################
# ### Tracks
# ### V 0.10
# #############################################################################
import defaults


# Bahnen der Schmutzteile
class Track_Seg:

    def __init__(self, num_pix, hit_rb_x, hit_rb_y):
        """Bahnen der Schmutzteile \n
        Direction = False -> Links nach Rechts \n
        Direction = True  -> Rechts nach Links \n
        Anzahl der LEDs \n
        Höhe der Kollision mit dem Radarstrahl"""
        self.num_pix = num_pix
        self.hit_rb_x = hit_rb_x    # Gibt die X Position an, auf den der Radar-Strahls die Bahn treffen könnte
        self.hit_rb_y = hit_rb_y    # Gibt die Höhe an, auf der der Rader-Strahl die Bahn treffen könnte
        self.direction = False

    def get_direction(self):
        return self.direction


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    my_tracks = []
    for i in range(defaults.Tracks.num_of_tracks):
        my_tracks.append(Track_Seg(defaults.Tracks.num_of_leds,
                                   defaults.Tracks.track_hit_x[i],
                                   defaults.Tracks.track_hit_y[i]))

    print(len(my_tracks))
    print(my_tracks[0].num_pix)
    print(my_tracks[0].direction)



# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
