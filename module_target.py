# #############################################################################
# ### Targets
# ### V 0.10
# #############################################################################
import time
import defaults


class Target:

    def __init__(self):
        """Schrottteile \n
        Position -> Links nach Rechts \n
        Track_num -> Bahn-Nummer"""
        self.position = 0
        self.track_num = 0
        self.activ_flag = False
        self.end_flag = False

    def next_position(self):
        if not self.end_flag:
            self.activ_flag = True
            if self.position < defaults.Tracks.num_of_leds:
                # print(self.position)
                self.position += 1
            else:
                # print("Target_End_Flag")
                self.end_flag = True
                self.activ_flag = False
                self.position = 0

    def get_position(self):
        return self.position

    def get_end_flag(self):
        return self.end_flag

    def set_new(self):
        self.end_flag = False
        self.activ_flag = False
        self.position = 0


# -----------------------------------------------------------------------------

def main():
    print("Start Global Init")
    my_targets = []
    for i in range(defaults.Target.num_of_targets):
        my_targets.append(Target())
    print(len(my_targets))


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# =============================================================================

# Radar Strahlen von Position 0 bis "end_flag"
# Bei Treffer mit Target -> Farbe auf Rot und zurück zur Position 0
