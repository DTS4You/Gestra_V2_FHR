# #############################################################################
# ### Tracks
# ### V 0.10
# #############################################################################

# Bahnen der Schmutzteile
class Track_Seg:

    def __init__(self, num_pix, hit_rb_y):
        """Bahnen der Schmutzteile \n
        Direction = False -> Links nach Rechts \n
        Direction = True  -> Rechts nach Links \n
        Anzahl der LEDs \n
        Höhe der Kollision mit dem Radarstrahl"""
        self.num_pix = num_pix
        self.hit_rb_y = hit_rb_y
        self.direction = False

    def get_direction(self):
        return self.direction


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    mg = Track_Seg(20, 10)
    print(mg.direction)
    print(mg.get_direction())


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================
