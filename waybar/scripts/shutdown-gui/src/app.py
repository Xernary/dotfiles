import tkinter as tk
import subprocess
import keyboard
from tkinter import PhotoImage

WINDOW_WIDTH = 400 
WINDOW_HEIGHT = 200
BUTTON_WIDTH = 32*3
BUTTON_HEIGHT = 32*3

IMAGES_PATH = "~/.config/waybar/scripts/shutdown-gui/res/"

BACKGROUND_COLOR = "#1E1E2E"

def run_power_command():
    subprocess.run(["shutdown", "now"])

def run_restart_command():
    subprocess.run(["reboot"])

root = tk.Tk()
root.title("Power Control")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg=BACKGROUND_COLOR)

frame = tk.Frame(root)
frame.pack(expand=True)
frame.configure(bg=BACKGROUND_COLOR)

power_icon = PhotoImage(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, file=IMAGES_PATH+"power-icon3.png")  # Placeholder icon
restart_icon = PhotoImage(width=BUTTON_WIDTH, height=BUTTON_HEIGHT, file=IMAGES_PATH+"arrow.png")  # Placeholder icon

power_button = tk.Button(frame, image=power_icon, bg="#F28FAD", command=run_power_command)
restart_button = tk.Button(frame, image=restart_icon, bg="#F8BD96", command=run_restart_command)

pad_x = ((WINDOW_WIDTH/2) - (BUTTON_WIDTH))/2
power_button.grid(row=0, column=0, padx=pad_x/1.5, pady=10)
restart_button.grid(row=0, column=1, padx=pad_x/1.5, pady=10)



root.mainloop()

