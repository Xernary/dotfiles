import tkinter as tk
import subprocess
from tkinter import PhotoImage, Canvas

def run_power_command():
    subprocess.run(["shutdown", "now"])

def run_restart_command():
    subprocess.run(["reboot"])

def create_rounded_button(canvas, x, y, width, height, radius, color, command):
    # Create a rounded rectangle
    canvas.create_oval(x, y, x + 2*radius, y + 2*radius, fill=color, outline=color)
    canvas.create_oval(x + width - 2*radius, y, x + width, y + 2*radius, fill=color, outline=color)
    canvas.create_oval(x, y + height - 2*radius, x + 2*radius, y + height, fill=color, outline=color)
    canvas.create_oval(x + width - 2*radius, y + height - 2*radius, x + width, y + height, fill=color, outline=color)
    canvas.create_rectangle(x + radius, y, x + width - radius, y + height, fill=color, outline=color)
    canvas.create_rectangle(x, y + radius, x + width, y + height - radius, fill=color, outline=color)
    
    button = tk.Button(root, text="", bg=color, activebackground=color, command=command, relief="flat", bd=0)
    button_window = canvas.create_window(x + width // 2, y + height // 2, window=button, width=width-10, height=height-10)
    return button

root = tk.Tk()
root.title("Power Control")
root.geometry("220x120")
root.resizable(False, False)

canvas = Canvas(root, width=220, height=120, bg="white", highlightthickness=0)
canvas.pack()

power_button = create_rounded_button(canvas, 20, 30, 80, 60, 20, "red", run_power_command)
restart_button = create_rounded_button(canvas, 120, 30, 80, 60, 20, "blue", run_restart_command)

root.mainloop()
