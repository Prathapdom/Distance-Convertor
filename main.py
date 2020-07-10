import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

# Enabling High DPI Awareness
try :
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except :
    pass

# Root window properties
root = tk.Tk()
root.title("Initial Setup")
root.geometry("300x200")
root.resizable(False, False)
style = ThemedStyle(root)
root.wm_iconbitmap('D:\Learning\Python\Code\Python\Desktop application\Bikini.ico')
style.set_theme('scidgrey')

root.columnconfigure(0, weight = 1)

# Variables
meter_value = tk.StringVar()
feet_value = tk.StringVar(value ="Feet Shows Here")

# Feet convertion function
def cal_feet(*args):
    try:
        meters = float(meter_value.get())
        feet = meters * 3.28084
        #print(f"{meters} meters is equal to {feet:.3f} feet.")
        feet_value.set(f"{feet:.3f} feet.")

    except ValueError:
        pass

# Frame and widgets declaration
main = ttk.Frame(root, padding=(30, 15)).grid()
meter_label = ttk.Label(main, text = "Meters:")
meter_input = ttk.Entry(main, width = 10, textvariable = meter_value)
calc_button = ttk.Button(main, text = "Calculate", command = cal_feet)

feet_label = ttk.Label(main, text = "Feet")
feet_dispaly = ttk.Label(main, textvariable = feet_value)

meter_label.grid(row = 0, column = 0, sticky = "W", padx = 5, pady = 5)
meter_input.grid(row = 0, column = 1, sticky = "EW", padx = 5, pady = 5)
meter_input.focus()

feet_label.grid(row = 1, column = 0, sticky = "W", padx = 5, pady = 5)
feet_dispaly.grid(row = 1, column = 1, sticky = "EW", padx = 5, pady = 5)

calc_button.grid(row = 2, column = 0, columnspan = 2, sticky = "EW", padx = 25, pady = 25)
root.bind("<Return>", cal_feet)
root.bind("<KP_Enter>", cal_feet)

root.mainloop()
