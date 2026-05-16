import tkinter as tk
from tkinter import ttk
import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

class AutoclickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Autoclicker")

        self.mouse = Controller()
        self.clicking = False
        self.click_button = Button.left
        self.cps = tk.DoubleVar(value=10.0)
        self.click_delay = 1.0 / self.cps.get()
        self.click_thread = None

        ttk.Label(master, text="Clicks Per Second (CPS):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.cps_entry = ttk.Entry(master, textvariable=self.cps, width=10)
        self.cps_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.cps_entry.bind("<FocusOut>", self.update_cps)
        self.cps_entry.bind("<Return>", self.update_cps)

        ttk.Label(master, text="Click Button:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.button_var = tk.StringVar(value="left")
        ttk.Radiobutton(master, text="Left", variable=self.button_var, value="left").grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Radiobutton(master, text="Right", variable=self.button_var, value="right").grid(row=1, column=2, padx=5, pady=2, sticky="w")

        self.toggle_button = ttk.Button(master, text="Start Autoclicker (0)", command=self.toggle_clicking)
        self.toggle_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10, sticky="ew")

        self.status_label = ttk.Label(master, text="Status: Idle")
        self.status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        self.keyboard_listener_thread = threading.Thread(target=self.start_keyboard_listener, daemon=True)
        self.keyboard_listener_thread.start()

        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

    def update_cps(self, event=None):
        try:
            new_cps = float(self.cps.get())
            if new_cps > 0:
                self.cps.set(new_cps)
                self.click_delay = 1.0 / self.cps.get()
            else:
                self.cps.set(10.0)
                self.click_delay = 0.1
                self.status_label.config(text="Status: Invalid CPS. Reset to 10.")
        except ValueError:
            self.cps.set(10.0)
            self.click_delay = 0.1
            self.status_label.config(text="Status: Invalid CPS. Reset to 10.")

    def clicker(self):
        while self.clicking:
            try:
                if self.button_var.get() == "left":
                    self.mouse.click(Button.left)
                elif self.button_var.get() == "right":
                    self.mouse.click(Button.right)
                time.sleep(self.click_delay)
            except Exception as e:
                print(f"Error during clicking: {e}")
                self.status_label.config(text=f"Status: Error - {e}")
                self.clicking = False
                self.toggle_button.config(text="Start Autoclicker (0)")

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.clicker, daemon=True)
            self.click_thread.start()
            self.status_label.config(text="Status: Autoclicking...")
            self.toggle_button.config(text="Stop Autoclicker (0)")

    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            self.status_label.config(text="Status: Idle")
            self.toggle_button.config(text="Start Autoclicker (0)")

    def toggle_clicking(self):
        if self.clicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def on_press(self, key):
        try:
            if key == KeyCode.from_char('0'):
                self.master.after(0, self.toggle_clicking)
            elif key == KeyCode.from_char('z'):
                self.master.after(0, lambda: self.button_var.set("left"))
                self.master.after(0, lambda: self.status_label.config(text="Status: Set to left click"))
            elif key == KeyCode.from_char('x'):
                self.master.after(0, lambda: self.button_var.set("right"))
                self.master.after(0, lambda: self.status_label.config(text="Status: Set to right click"))
            elif key == Key.esc:
                self.master.destroy()
                return False
        except AttributeError:
            pass

    def start_keyboard_listener(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    root = tk.Tk()
    gui = AutoclickerGUI(root)
    root.mainloop()