import nidaqmx as daq
import math
import customtkinter as tk
import time



def reset():
        # move all the way to (0,0) coordinate. Once it hits the button it well set that as a 0,0 coordinate
        task_read_button = daq.Task()
        task_read_button.ai_channels.add_ai_voltage_chan('Dev1/ai4')
        at_start = False
        while at_start != True:
            move_pos()
            data = task_read_button.read(number_of_samples_per_channel=1)
            data = int(data[0])
            print(data)
            if data == 0:
                  at_start = True
        
        task_read_button.close()
        return

def move_neg():
        # Creating a task might take extra time maybe try way to implement in the init fnction to create task
        # Must send on and off signal for each step
        task1 = daq.Task()
        task1.do_channels.add_do_chan('dev1/port1/line0') 
        task1.write(True)
        time.sleep(0.00016)
        task1.write(False)
        time.sleep(0.00016)
        task1.stop()
        task1.close()
        
def move_pos():
        task1 = daq.Task()
        task2 = daq.Task()
        task1.do_channels.add_do_chan('dev1/port1/line0') 
        task2.do_channels.add_do_chan('dev1/port1/line1') 
        task2.write(True)
        # Must send on and off signal for each step
        task1.write(True)
        time.sleep(0.00008)
        task1.write(False)
        time.sleep(0.00008)
        task2.write(False)
        task2.stop()
        task1.stop()
        task1.close()
        task2.close()

reset()