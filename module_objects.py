# #############################################################################
# ### Objets
# ### V 0.10
# #############################################################################
import time

import defaults
import module_radar
import module_target
import module_tracks
from module_spi import SPI
import random


class State_Machine():

    def __init__(self, wait_cycles=2):
        self.wait_cycles        = wait_cycles               # Wartezyklen bis ein neues Schrottteil erzeugt wird
        self.wait_counter       = 0                         # Zähler für Wartezyklen
        self.new_flag           = True
        self.step_target_flag   = False                     # Nächtste Target Position
        self.max_target_flag    = False                     # Maximale Anzahl der Schrottteile erreicht
        self.radar_end_flag     = False                     # Alle Radar-Strahlen sind am Ende

    def next_step(self):
        if self.check_radar_end():
            print("New Radar sequence")
            self.next_target_pos()
            self.reset_radar_pos()

        else:
            print("Next Radar position")
            for i in range(len(radar_beams)):
                radar_beams[i].next_position()
                print("Radar_Pos: ", radar_beams[i].get_position())

    def reset_radar_pos(self):
        for i in range(len(radar_beams)):
            radar_beams[i].set_new()
        self.radar_end_flag = False
        self.new_flag = True
        return self.new_flag

    def next_target_pos(self):
        for i in range(len(targets)):
            print("Target_Pos: ", targets[i].get_position())
        self.step_target_flag = True

    def next_target(self):
        if self.wait_counter < self.wait_cycles:
            self.wait_counter += 1
        else:
            self.wait_counter = 0
            self.new_flag = False
            self.wait_cycles = random.randint(defaults.Values.wait_cycle_min, defaults.Values.wait_cycle_max)

    def check_radar_end(self):
        for i in range(len(radar_beams)):
            self.radar_end_flag = self.radar_end_flag or radar_beams[i].get_end_flag()
        return self.radar_end_flag


def check_max_targets():
    num_of_activ_targets = 0
    for i in range(len(targets)):
        if targets[i].activ_flag:
            num_of_activ_targets += 1
    if num_of_activ_targets == len(targets):
        state_logic.max_target_flag = True
    else:
        state_logic.max_target_flag = False


def generate_radar_beams():
    my_radar_beams = []
    for i in range(defaults.Radar_Beams.num_of_beams):
        my_radar_beams.append(module_radar.Radar_Beam(defaults.Radar_Beams.num_of_leds))
    return my_radar_beams


def generate_radar_reflect():
    my_radar_reflects = []
    for i in range(defaults.Radar_Reflect.num_of_beams):
        my_radar_reflects.append(module_radar.Radar_Reflect(defaults.Radar_Reflect.num_of_leds))
    return my_radar_reflects


def generate_targets():
    my_targets = []
    for i in range(defaults.Target.num_of_targets):
        my_targets.append(module_target.Target())
    return my_targets


def generate_tracks():
    my_tracks = []
    for i in range(defaults.Tracks.num_of_tracks):
        my_tracks.append(module_tracks.Track_Seg(defaults.Tracks.num_of_leds,
                                                 defaults.Tracks.direction[i],
                                                 defaults.Tracks.track_hit_x[i],
                                                 defaults.Tracks.track_hit_y[i]
                                                 ))
    return my_tracks


def init_ddbs():
    for i in range(defaults.DDB.num_of_ddbs):
        ddb.ddb_init(i, 40)


def ddbs_default():
    for i in range(defaults.DDB.num_of_ddbs):
        ddb.ddb_set_rgb(i, 0, 0, 10)
        ddb.ddb_set_all(i)
        time.sleep_ms(20)
        ddb.ddb_show(i)

def generate_objects():
    global state_logic, tracks, targets, radar_beams, radar_reflects, ddb
    print("Generate Objects")
    tracks = generate_tracks()
    targets = generate_targets()
    radar_beams = generate_radar_beams()
    radar_reflects = generate_radar_reflect()
    state_logic = State_Machine()
    ddb = SPI()


# -----------------------------------------------------------------------------

def main():
    print("Start Objects")
    generate_objects()
    i = 0
    while i < 50:
        state_logic.next_step()
        #print(state_logic.check_radar_end())
        #print(state_logic.wait_cycles)
        i += 1
        time.sleep(0.3)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    print("=== End of Program ===")

# =============================================================================
