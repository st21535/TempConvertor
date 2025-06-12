from tkinter import *

class Temperature:
    def __init__(self):
        self.root = Tk()
        self.root.title("Convert Temperature")

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nswe")

        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()
        

        self.show_frame("MainFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def create_main_frame(self):
        frame = Frame(self.container)

        self.temp_converter_label = Label(frame, font="Arial 16", text="Temperature Converter")
        self.temp_converter_label.grid(row=0, columnspan=2, padx=10, pady=10)

        self.to_c_button = Button(frame, text="To Centigrade", bg="#dda6aa", font="Arial 12 ", 
                                  command=lambda: self.show_frame("to_cFrame"))
        self.to_c_button.grid(row=1, column=0, padx=10, pady=10)

        self.to_f_button = Button(frame, text="To Fahrenheit", bg="#dda6aa", font="Arial 12", 
                                  command=lambda: self.show_frame("to_fFrame"))
        self.to_f_button.grid(row=1, column=1, padx=10, pady=10)

        frame.grid(row=0, column=0, sticky="nswe")

        for i in range(2):
            frame.grid_columnconfigure(0,weight=1)
        for i in range(2):
            frame.grid_rowconfigure(0,weight=1)
        return frame

    def create_to_c_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nswe")
        Label(frame, text="Convert to Celsius").grid(row=0, column=1)
        
        
        self.temp_entry_c=Entry(frame, justify=CENTER)
        self.temp_entry_c.grid(row=1,column=1) 

        self.result_label_c = Label(frame, text="Result: ")
        self.result_label_c.grid(row=3, column=0, columnspan=2, pady=10)


        self.calc_button = Button(frame, text="Calculate", bg="#dda6aa",font="Arial 12",command=self.calc_to_c)
        self.calc_button.grid(row=2,column=1, padx=10,pady=10)

        self.back_button = Button(frame, text="Go Back", bg="#dda6aa", font="Arial 12 ",command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button=Button(frame, text="Reset", bg="#dda6aa", font="Arial 12", command=self.reset)
        self.reset_button.grid(row=2,column=2,padx=10,pady=10)

        return frame

    def create_to_f_frame(self):
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nswe")
        Label(frame, text="Convert to Fahrenheit").grid(row=0, column=1)
        
        
        self.temp_entry_f=Entry(frame, justify=CENTER)
        self.temp_entry_f.grid(row=1,column=1) 

        self.result_label_f = Label(frame, text="Result: ")
        self.result_label_f.grid(row=3, column=0, columnspan=2, pady=10)


        self.calc_button = Button(frame, text="Calculate", bg="#dda6aa",font="Arial 12",command=self.calc_to_f)
        self.calc_button.grid(row=2,column=1, padx=10,pady=10)

        self.back_button = Button(frame, text="Go Back", bg="#dda6aa", font="Arial 12 ",command=lambda: self.show_frame("MainFrame"))
        self.back_button.grid(row=2, column=0, padx=10, pady=10)

        self.reset_button=Button(frame, text="Reset", bg="#dda6aa", font="Arial 12",command=self.reset)
        self.reset_button.grid(row=2,column=2,padx=10,pady=10)

        return frame
    
    def calc_to_f(self):
        try:
            temp = float(self.temp_entry_f.get())
            farenhright=(temp*9/5)+32
            self.result_label_f.config(text=f"Result: {farenhright:.2f}°F")
        except ValueError:
            self.result_label_f.config(text="Invalid input! Enter a number.")
 
    def calc_to_c(self):
        try:
            temp = float(self.temp_entry_c.get())
            farenhright=(temp-32)*5/9
            self.result_label_c.config(text=f"Result: {farenhright:.2f}°F")
        except ValueError:
            self.result_label_c.config(text="Invalid input! Enter a number.")
    def reset(self):
        self.temp_entry_c.delete(0, END) 
        self.temp_entry_f.delete(0, END)  
        self.result_label_c.config(text="Result: ") 
        self.result_label_f.config(text="Result: ")  

    def run(self):
        self.root.mainloop()

Temperature().run()
