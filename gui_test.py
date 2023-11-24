
import customtkinter as tk
import math
import energy_frame as ef

'''

    First window of the pdt software for control of the automated robotic system.
    
'''
class myGUI(tk.CTkToplevel):
    def __init__(self):
        
        # Basic setup of the window
        self.root = tk.CTk()
        self.root.title('LED Array')
        self.root.geometry('1920x1080')
        tk.set_default_color_theme('dark-blue')

        # Setup of the first drop menu for the well plate size
        self.options_well = ['96 Well Plates', '24 Well Plates']
        clicked_well = tk.StringVar()
        clicked_well.set('96 Well Plates')
        self.drop_menu_well = tk.CTkOptionMenu(self.root, font=('Arial', 18), variable = clicked_well,values = self.options_well)
        self.drop_menu_well.grid(row=1,column = 1, padx = 20,pady = 20)

        # setu of the second drop down menu for config
        self.options_pdt_config = ['2x2','3x3','2x3','2x4']
        clicked_pdt_config = tk.StringVar()
        clicked_pdt_config.set('2x2')
        self.drop_menu_config = tk.CTkOptionMenu(self.root, font=('Arial',18), variable = clicked_pdt_config, values = self.options_pdt_config)
        self.drop_menu_config.grid(row=2,column =1, padx=20,pady=20)

        # Labels clearing indicating what each drop down menu is
        label_well_opt = tk.CTkLabel(self.root,text='Well Plate Size:', font=("Arial",18))
        label_well_opt.grid(row=1,column=0,padx=20,pady=20)

        label_pdt_config = tk.CTkLabel(self.root,text='PDT Configuration:',font=("Arial",18))
        label_pdt_config.grid(row=2,column=0,padx=20,pady=20)

        # Opening up other menu to input engery 
        btn1 = tk.CTkButton(self.root,text='Activate',font=('Arial',18), command = lambda : self.activate())
        btn1.grid(row=4,column=1,padx=100,pady=100,sticky='w')

        # Main loop 
        self.root.mainloop()
    
    def activate(self):
        
        well_plate = self.drop_menu_well.get()
        config = self.drop_menu_config.get()
        well_plate_value, config_box = self.dimensions(well_plate,config)
        num_boxes = math.floor(well_plate_value/config_box)
        ef.text_input_frame(num_boxes,well_plate_value,config_box)
        return
    
    def dimensions(self,well_plate,config):

        well_dict = {'96 Well Plates': 96,
                     '24 Well Plates': 24}
        config_dict = {'2x2':4,
                       '2x3':6,
                       '2x4':8,
                       '3x3':9}
        
        well_plate_value = well_dict[well_plate]
        config_box = config_dict[config]

        return well_plate_value,config_box

# Runs everything
myGUI()


