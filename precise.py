import nidaqmx as daq
import matplotlib.pyplot as plt
import time 
import numpy as np 

def precise_fun():
    task1 = daq.Task()
    task2 = daq.Task()
    task1.ao_channels.add_ao_voltage_chan('Dev2/ao0')
    task2.ai_channels.add_ai_voltage_chan('Dev2/ai0')

    counter = 0
    listy = []
    task1.write(1, auto_start=True)
    while counter < 10: 
        data = task2.read(number_of_samples_per_channel=1)
        listy.append(data)
        counter+=1
        time.sleep(0.1)
    task1.stop()
    counter2=0
    task1.write(0,auto_start=True)
    while counter2 < 10:
        data = task2.read(number_of_samples_per_channel=1)
        listy.append(data)
        counter2+=1
        time.sleep(0.1)
    task1.stop()
    task2.stop()

    plt.plot(np.linspace(0,2,20),listy)
    plt.show()

    task1.close()
    task2.close()
precise_fun()


