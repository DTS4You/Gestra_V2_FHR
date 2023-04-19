# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 0.11                                                                ***
# *****************************************************************************

import time
import defaults

loop_time = defaults.Values.loop_time


class Logic:

    def __init__(self):
        self.input_state = [ False, False, False, False]
        self.output_flag = False

    def set_state(self, num):
        self.input_state[num] = True

    def clear_state(self, num):
        self.input_state[num] = False

    def check_state_or(self):
        for i in range(len(self.input_state)):
            self.output_flag = self.output_flag or self.input_state[i]
        return self.output_flag


array = [0, 1, 2, 3]


# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")

    print(array)

    new_array = array[::-1]
    print(new_array)

    i = 0

    logic = Logic()

    while i < 100:
        if i == 5:
            logic.set_state(0)
        else:
            logic.clear_state(0)
        # print(logic.input_state[0], logic.input_state[1], logic.input_state[2], logic.input_state[3])
        #print(logic.input_state)
        #print(logic.check_state_or())
        time.sleep(loop_time)
        i += 1


# =============================================================================
if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")
# =============================================================================