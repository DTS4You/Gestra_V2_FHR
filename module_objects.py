# #############################################################################
# ### Objects
# ### V 0.11
# #############################################################################
import time
import defaults
import module_i2c
import module_radar
import module_target
import module_tracks
from module_spi import SPI
from lib.neopixel import Neopixel
import random

global state_logic, tracks, targets, radar_beams, radar_reflects, ddb, stripe, gpio


class State_Machine():

    def __init__(self, wait_cycles=2):
        self.wait_cycles = wait_cycles  # Wartezyklen bis ein neues Schrottteil erzeugt wird
        self.wait_counter = 0  # Zähler für Wartezyklen
        self.new_flag = True
        self.step_target_flag = False  # Nächtste Target Position
        self.max_target_flag = False  # Maximale Anzahl der Schrottteile erreicht
        self.radar_end_flag = False  # Alle Radar-Strahlen sind am Ende

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
    my_radar_beams[0].offset = defaults.Radar_Reflect.num_of_leds[0] + defaults.Radar_Reflect.num_of_leds[1] + \
                                   defaults.Radar_Reflect.num_of_leds[2] + defaults.Radar_Reflect.num_of_leds[3]
    my_radar_beams[0].ddb = defaults.Radar_Beams.ddb[0]
    my_radar_beams[1].offset = defaults.Radar_Reflect.num_of_leds[4] + defaults.Radar_Reflect.num_of_leds[5] + \
                                   defaults.Radar_Reflect.num_of_leds[6] + defaults.Radar_Reflect.num_of_leds[7]
    my_radar_beams[1].ddb = defaults.Radar_Beams.ddb[1]
    my_radar_beams[2].offset = defaults.Radar_Reflect.num_of_leds[8] + defaults.Radar_Reflect.num_of_leds[9] + \
                                   defaults.Radar_Reflect.num_of_leds[10] + defaults.Radar_Reflect.num_of_leds[11]
    my_radar_beams[2].ddb = defaults.Radar_Beams.ddb[2]
    my_radar_beams[3].offset = defaults.Radar_Reflect.num_of_leds[12] + defaults.Radar_Reflect.num_of_leds[13] + \
                                   defaults.Radar_Reflect.num_of_leds[14] + defaults.Radar_Reflect.num_of_leds[15]
    my_radar_beams[3].ddb = defaults.Radar_Beams.ddb[3]
    return my_radar_beams


def generate_radar_reflect():
    my_radar_reflects = []
    for i in range(defaults.Radar_Reflect.num_of_beams):
        my_radar_reflects.append(module_radar.Radar_Reflect(defaults.Radar_Reflect.num_of_leds[i],
                                                            defaults.Radar_Reflect.direction[i]))
    my_radar_reflects[0].offset = 0
    my_radar_reflects[1].offset = defaults.Radar_Reflect.num_of_leds[0]
    my_radar_reflects[2].offset = my_radar_reflects[1].offset + defaults.Radar_Reflect.num_of_leds[1]
    my_radar_reflects[3].offset = my_radar_reflects[2].offset + defaults.Radar_Reflect.num_of_leds[2]
    my_radar_reflects[4].offset = 0
    my_radar_reflects[5].offset = defaults.Radar_Reflect.num_of_leds[4]
    my_radar_reflects[6].offset = my_radar_reflects[5].offset + defaults.Radar_Reflect.num_of_leds[5]
    my_radar_reflects[7].offset = my_radar_reflects[6].offset + defaults.Radar_Reflect.num_of_leds[6]
    my_radar_reflects[8].offset = 0
    my_radar_reflects[9].offset = defaults.Radar_Reflect.num_of_leds[8]
    my_radar_reflects[10].offset = my_radar_reflects[9].offset + defaults.Radar_Reflect.num_of_leds[9]
    my_radar_reflects[11].offset = my_radar_reflects[10].offset + defaults.Radar_Reflect.num_of_leds[10]
    my_radar_reflects[12].offset = 0
    my_radar_reflects[13].offset = defaults.Radar_Reflect.num_of_leds[12]
    my_radar_reflects[14].offset = my_radar_reflects[13].offset + defaults.Radar_Reflect.num_of_leds[13]
    my_radar_reflects[15].offset = my_radar_reflects[14].offset + defaults.Radar_Reflect.num_of_leds[14]
    my_radar_reflects[0].ddb = defaults.Radar_Reflect.num_of_ddb[0]
    my_radar_reflects[1].ddb = defaults.Radar_Reflect.num_of_ddb[1]
    my_radar_reflects[2].ddb = defaults.Radar_Reflect.num_of_ddb[2]
    my_radar_reflects[3].ddb = defaults.Radar_Reflect.num_of_ddb[3]
    my_radar_reflects[4].ddb = defaults.Radar_Reflect.num_of_ddb[4]
    my_radar_reflects[5].ddb = defaults.Radar_Reflect.num_of_ddb[5]
    my_radar_reflects[6].ddb = defaults.Radar_Reflect.num_of_ddb[6]
    my_radar_reflects[7].ddb = defaults.Radar_Reflect.num_of_ddb[7]
    my_radar_reflects[8].ddb = defaults.Radar_Reflect.num_of_ddb[8]
    my_radar_reflects[9].ddb = defaults.Radar_Reflect.num_of_ddb[9]
    my_radar_reflects[10].ddb = defaults.Radar_Reflect.num_of_ddb[10]
    my_radar_reflects[11].ddb = defaults.Radar_Reflect.num_of_ddb[11]
    my_radar_reflects[12].ddb = defaults.Radar_Reflect.num_of_ddb[12]
    my_radar_reflects[13].ddb = defaults.Radar_Reflect.num_of_ddb[13]
    my_radar_reflects[14].ddb = defaults.Radar_Reflect.num_of_ddb[14]
    my_radar_reflects[15].ddb = defaults.Radar_Reflect.num_of_ddb[15]
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
                                                 defaults.Tracks.offset[i],
                                                 defaults.Tracks.direction[i],
                                                 defaults.Tracks.track_hit_y[i],
                                                 defaults.Tracks.track_hit_z[i]
                                                 ))
    return my_tracks


def ddbs_init():
    for i in range(defaults.DDB.num_of_ddbs):
        ddb.ddb_init(i, radar_beams[i].offset + radar_beams[i].num_pix)
        # print(radar_beams[i].offset + radar_beams[i].num_pix)


def ddbs_default():
    for i in range(defaults.DDB.num_of_ddbs):
        ddb.ddb_set_rgb(i, 0, 0, 10)
        ddb.ddb_set_all(i)
        time.sleep_ms(20)
        ddb.ddb_show(i)


def ws2812_defaults():
    for i in range(len(stripe)):
        stripe[i].brightness(255)
        stripe[i].fill((0, 0, 10))
        stripe[i].show()


def ddbs_start_stop():
    for i in range(4):
        set_pixel_ddb_beams(i, 0, defaults.Colors.start)
        set_pixel_ddb_beams(i, radar_beams[i].num_pix - 1, defaults.Colors.end)
    for i in range(16):
        set_pixel_ddb_reflect(i, 0, defaults.Colors.start)
        set_pixel_ddb_reflect(i, radar_reflects[i].num_pix - 1, defaults.Colors.end)
    ddb.ddb_show(0)
    ddb.ddb_show(1)
    ddb.ddb_show(2)
    ddb.ddb_show(3)


def set_pixel_ddb_beams(beam, pos, color=defaults.Colors.default):
    r = color[0]
    g = color[1]
    b = color[2]
    ddb_num = radar_beams[beam].ddb
    ddb.ddb_set_rgb(ddb_num, r, g, b)
    ddb.ddb_set_led(ddb_num, pos + radar_beams[beam].offset)


def set_pixel_ddb_reflect(beam, pos, color=defaults.Colors.default):
    r = color[0]
    g = color[1]
    b = color[2]
    ddb_num = radar_reflects[beam].ddb
    ddb.ddb_set_rgb(ddb_num, r, g, b)
    if radar_reflects[beam].direction:
        # print("Top-Bot")
        pos = radar_reflects[beam].num_pix - pos - 1
    else:
        # print("Bot-Top")
        pass
    ddb.ddb_set_led(ddb_num, pos + radar_reflects[beam].offset)


def ws2812_set_pixel(target, pos, color=defaults.Colors.default):       # !!! New
    r, b, g = color
    _stripe = targets[target].track_num
    print(_stripe, pos, r, g, b)


def gpio_set_output(value):
    gpio.set_output(0, value)


def gpio_get_input():
    return gpio.get_input(8)


def generate_objects():
    global state_logic, tracks, targets, radar_beams, radar_reflects, ddb, stripe, gpio
    print("Generate Objects")
    tracks = generate_tracks()
    targets = generate_targets()
    radar_beams = generate_radar_beams()
    radar_reflects = generate_radar_reflect()
    state_logic = State_Machine()
    ddb = SPI()                                 # SPI-Funktionen für Digi-Dot-Booster Module
    stripe = []                                 # WS2812-PIO vorbereiten und anlegen
    for i in range(defaults.Stripe.num_of_stripes):
        stripe.append(Neopixel(defaults.Stripe.num_of_leds,
                               defaults.Stripe.pio_no[i],
                               defaults.Stripe.pin_no[i],
                               "GRB"))
    gpio = module_i2c.GPIO()


# -----------------------------------------------------------------------------

def main():
    print("Start Objects")
    generate_objects()
    ddbs_init()
    ddbs_default()
    ws2812_defaults()
    for i in range(4):
        set_pixel_ddb_beams(i, 0, defaults.Colors.start)
        set_pixel_ddb_beams(i, radar_beams[i].num_pix - 1, defaults.Colors.end)
    for i in range(16):
        set_pixel_ddb_reflect(i, 0, defaults.Colors.start)
        set_pixel_ddb_reflect(i, radar_reflects[i].num_pix - 1, defaults.Colors.end)
    ddb.ddb_show(0)
    ddb.ddb_show(1)
    ddb.ddb_show(2)
    ddb.ddb_show(3)
    # i = 0
    # while i < 50:
    #    state_logic.next_step()
    #    #print(state_logic.check_radar_end())
    #    #print(state_logic.wait_cycles)
    #    i += 1
    #    time.sleep(0.3)


# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    print("=== End of Program ===")

# =============================================================================
