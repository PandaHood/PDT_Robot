import customtkinter as tk
import math
import move 

class text_input_frame:
    def __init__(self, box_num,well_plate_value,config_box):
        self.root = tk.CTk()

        self.root.title('Energy Input')
        self.root.geometry('1920x1080')
        tk.set_default_color_theme('dark-blue')
        
        self.box_num = box_num
        self.text_box_list = list()
        for _ in range(box_num):
            self.text_box_list.append(tk.CTkTextbox(self.root, height = 1, width = 50, wrap = None ))
        j = 1
        i = 0
        self.well_p, self.config_b = self.dimensions(well_plate_value,config_box)
        for x in range(box_num):
            if i >= math.floor(self.well_p/self.config_b):
                j += 1
                i = 0
            self.text_box_list[x].grid(row = j, column = i, padx = 25, pady = 25)
            i += 1

        btnrun = tk.CTkButton(self.root,text='Run',font=('Arial',18), command = lambda : self.run())
        btnrun.grid(row = 0,column=0,padx = 5,pady = 5,sticky = 'w')

        self.root.mainloop()
    
    def run(self):
        self.get_value()
        self.algo()
        return 
        
    def dimensions(self,w,c):
        config_dict = {4:2,
                       6:3,
                       8:4,
                       9:3}
        well_dict = {96:12, 
                     24:6}
        return well_dict[w],config_dict[c]

    def get_value(self):
        self.text_value_list = []

        for i in range(self.box_num):
            self.text_value_list.append(self.text_box_list[i].get('1.0','end'))
        
        self.new_value_list = []
        for i in range(len(self.text_value_list)):
            temp = []
            for j in range(len(self.text_value_list[i])):
                if self.text_value_list[i][j] in '0123456789':
                    temp.append(self.text_value_list[i][j])         
            self.new_value_list.append(''.join(temp))
        #print(self.new_value_list)
        for i in range(len(self.new_value_list)):
            try:
                self.new_value_list[i] = float(self.new_value_list[i])
            except ValueError:
                self.new_value_list[i] = float(0)

    def algo(self):
        armx = move.arm('Dev1/port1/line0','dev1/port1/line1',math.floor(self.well_p/self.config_b))
        #army = move.arm('','')
        
        # reseting arm to (0,0)
        armx.reset()
        #army.reset()
        armx.close()

        # Moving plate to first well
        #armx.move_to_first_well()
        #army.move_to_first_well()

        # begin loop
        #i = 1
        #while i != (len(self.new_value_list)):
            
            

        # Reset arms back to (0,0)