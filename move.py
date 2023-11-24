import nidaqmx as daq
import time


class arm:

    def __init__(self, port_neg, port_pos_activate, tmp):
        self.port_neg = port_neg # replace with port_pos 
        self.port_pos_activate = port_pos_activate # replace with ort_neg 
        self.coord = 0
        self.task1 = daq.Task()
        self.task2 = daq.Task()
        self.task1.do_channels.add_do_chan(self.port_neg) 
        self.task2.do_channels.add_do_chan(self.port_pos_activate)

        self.one_step = 0.016 # slow speed
        self.fast_speed = 0.00016
        

    def reset(self):
        # move all the way to (0,0) coordinate. Once it hits the button it well set that as a 0,0 coordinate
        task_read_button = daq.Task()
        task_read_button.ai_channels.add_ai_voltage_chan('Dev1/ai4')
        at_start = False
        while at_start != True:
            self.move_neg()
            data = task_read_button.read(number_of_samples_per_channel=1)
            if int(data[0]) == 0:
                  at_start = True
        
        task_read_button.close()
        return

    def move_pos(self):

        self.task2.write(True)
        # Must send on and off signal for each step
        self.task1.write(True)
        time.sleep(0.016)
        self.task1.write(False)
        time.sleep(0.016)
        self.task2.write(False)
        self.coord += 1

    def move_neg(self):
        start = time.time()
        # # Must send on and off signal for each step
        # self.task1.write(True)
        # time.sleep(0.000008)
        # self.task1.write(False)
        # time.sleep(0.000008)
        self.task1.timing.cfg_samp_clk_timing(rate=1000)
        self.task1.write([10,0,10,0,10,0,10,0])
        self.task1.wait_until_done()




        end = time.time()

        print(end - start)

    def move_to_first_well(self):
        pass

    def move_between_wells(self):
        pass

    def max_power_move(self):
        pass

    def read_phototransitor(self):
        pass

    def close(self):
        self.task1.stop()
        self.task2.stop()
        self.task1.close()
        self.task2.close()



#{
# Basic Movement algorthm 
# Movement distance and motor speed (5mm/200)
# OOP for coordinates 
# take input for from photo transnisotr
# 
# Set up intake for phototransistor
# fine tuning spot for using input from photo transistor 
# }

    
    
