from tkinter import *

class Temperature:
    def __init__(self):
        self.root = Tk()
        self.root.title("Convert Temperature")
        self.root.geometry("400x400")
        self.root.configure(bg="#6c7228")

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

        self.to_c_button = Button(frame, text="To Centigrade", bg="#ff3240", font="Arial 12 ", 
                                  command=lambda: self.show_frame("to_cFrame"))
        self.to_c_button.grid(row=1, column=0, padx=10, pady=10)

        self.to_f_button = Button(frame, text="To Fahrenheit", bg="#4a070c", font="Arial 12", 
                                  command=lambda: self.show_frame("to_fFrame"))
        self.to_f_button.grid(row=1, column=1, padx=10, pady=10)

        frame.grid(row=0, column=0, sticky="nswe")
        return frame

    def create_to_c_frame(self):
        frame = Frame(self.container)
        Label(frame, text="Convert to Centigrade").grid(row=0, column=0)
        frame.grid(row=0, column=0, sticky="nswe")
        return frame

    def create_to_f_frame(self):
        frame = Frame(self.container)
        Label(frame, text="Convert to Fahrenheit").grid(row=0, column=0)
        frame.grid(row=0, column=0, sticky="nswe")
        return frame

    def run(self):
        self.root.mainloop()

Temperature().run()