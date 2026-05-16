import tkinter as tk
from tkinter import ttk
import threading
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Listener, KeyCode, Key

class AutoclickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Autoclicker")

        self.mouse = MouseController()
        self.keyboard = KeyboardController() # New: Keyboard controller
        self.clicking = False
        self.click_type_var = tk.StringVar(value="left_mouse") # New: To select click type
        self.cps = tk.DoubleVar(value=10.0)
        self.click_delay = 1.0 / self.cps.get()
        self.click_thread = None

        self.toggle_key_var = tk.StringVar(value='0')
        self.current_listener = None

        ttk.Label(master, text="Clicks Per Second (CPS):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.cps_entry = ttk.Entry(master, textvariable=self.cps, width=10)
        self.cps_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.cps_entry.bind("<FocusOut>", self.update_cps)
        self.cps_entry.bind("<Return>", self.update_cps)

        # New: Click Type selection
        ttk.Label(master, text="Click Type:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(master, text="Left Mouse", variable=self.click_type_var, value="left_mouse").grid(row=1, column=1, padx=5, pady=2, sticky="w")
        ttk.Radiobutton(master, text="Right Mouse", variable=self.click_type_var, value="right_mouse").grid(row=1, column=2, padx=5, pady=2, sticky="w")
        ttk.Radiobutton(master, text="Spacebar", variable=self.click_type_var, value="spacebar").grid(row=2, column=1, padx=5, pady=2, sticky="w") # Moved to row 2

        # Existing Toggle Hotkey (now on row 3)
        ttk.Label(master, text="Toggle Hotkey:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.toggle_key_entry = ttk.Entry(master, textvariable=self.toggle_key_var, width=5)
        self.toggle_key_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.toggle_key_entry.bind("<FocusOut>", self.update_toggle_key)
        self.toggle_key_entry.bind("<Return>", self.update_toggle_key)
        self.toggle_key_entry.bind("<Key>", self.set_toggle_key_on_keypress)

        self.toggle_button = ttk.Button(master, text=f"Start Autoclicker ({self.toggle_key_var.get()})", command=self.toggle_clicking)
        self.toggle_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10, sticky="ew") # Moved to row 4

        self.status_label = ttk.Label(master, text="Status: Idle")
        self.status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="w") # Moved to row 5

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
                self.status_label.config(text="Status: CPS updated.")
            else:
                self.cps.set(10.0)
                self.click_delay = 0.1
                self.status_label.config(text="Status: Invalid CPS. Reset to 10.")
        except ValueError:
            self.cps.set(10.0)
            self.click_delay = 0.1
            self.status_label.config(text="Status: Invalid CPS. Reset to 10.")

    def set_toggle_key_on_keypress(self, event):
        key_char = event.char
        if key_char:
            self.toggle_key_var.set(key_char)
            self.update_toggle_key()
            self.toggle_key_entry.master.focus_set()
        return "break"

    def update_toggle_key(self, event=None):
        current_key = self.toggle_key_var.get()
        if not current_key:
            self.toggle_key_var.set('0')
            self.status_label.config(text="Status: Toggle key reset to '0'.")
        self.toggle_button.config(text=f"Start Autoclicker ({self.toggle_key_var.get()})")

        if self.current_listener:
            self.current_listener.stop()
            # It's good practice to join the thread to ensure it's fully stopped
            # before potentially starting a new one.
            # However, the listener is daemon, so the main program exiting will kill it.
            # For a re-start scenario, starting a new thread might be more robust
            # than relying on the old one to re-evaluate on_press logic immediately.
            # For simplicity here, we rely on the on_press picking up the new var.
            pass

        self.status_label.config(text=f"Status: Toggle hotkey set to '{self.toggle_key_var.get()}'.")


    def clicker(self):
        while self.clicking:
            try:
                click_type = self.click_type_var.get()
                if click_type == "left_mouse":
                    self.mouse.click(Button.left)
                elif click_type == "right_mouse":
                    self.mouse.click(Button.right)
                elif click_type == "spacebar":
                    self.keyboard.press(Key.space)
                    self.keyboard.release(Key.space)
                time.sleep(self.click_delay)
            except Exception as e:
                print(f"Error during clicking: {e}")
                self.status_label.config(text=f"Status: Error - {e}")
                self.clicking = False
                self.toggle_button.config(text=f"Start Autoclicker ({self.toggle_key_var.get()})")

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.clicker, daemon=True)
            self.click_thread.start()
            self.status_label.config(text="Status: Autoclicking...")
            self.toggle_button.config(text=f"Stop Autoclicker ({self.toggle_key_var.get()})")

    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            self.status_label.config(text="Status: Idle")
            self.toggle_button.config(text=f"Start Autoclicker ({self.toggle_key_var.get()})")

    def toggle_clicking(self):
        if self.clicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def on_press(self, key):
        try:
            custom_toggle_key_char = self.toggle_key_var.get()
            if len(custom_toggle_key_char) == 1 and key == KeyCode.from_char(custom_toggle_key_char):
                self.master.after(0, self.toggle_clicking)
            elif key == KeyCode.from_char('z'):
                self.master.after(0, lambda: self.click_type_var.set("left_mouse"))
                self.master.after(0, lambda: self.status_label.config(text="Status: Click type set to Left Mouse"))
            elif key == KeyCode.from_char('x'):
                self.master.after(0, lambda: self.click_type_var.set("right_mouse"))
                self.master.after(0, lambda: self.status_label.config(text="Status: Click type set to Right Mouse"))
            elif key == KeyCode.from_char('c'): # New: Hotkey for Spacebar click type
                self.master.after(0, lambda: self.click_type_var.set("spacebar"))
                self.master.after(0, lambda: self.status_label.config(text="Status: Click type set to Spacebar"))
            elif key == Key.esc:
                self.master.destroy()
                if self.current_listener:
                    self.current_listener.stop()
                return False
        except AttributeError:
            pass

    def start_keyboard_listener(self):
        if self.current_listener and self.current_listener.running:
            self.current_listener.stop()
            # You might want to add a short sleep here if you observe issues with quick restarts
            # time.sleep(0.1)
            # No need to join a daemon thread if it's being replaced, but it doesn't hurt.

        with Listener(on_press=self.on_press) as listener:
            self.current_listener = listener
            listener.join()

if __name__ == "__main__":
    root = tk.Tk()
    gui = AutoclickerGUI(root)
    root.mainloop()