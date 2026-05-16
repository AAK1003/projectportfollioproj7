import tkinter as tk
from tkinter import messagebox

# ==========================================
# YOUR EXACT LOGIC & STATE (Adapted for GUI)
# ==========================================

task_list = []


def update_display():
    """Helper function to refresh the visual list box"""
    list_box.delete(0, tk.END)
    for task in task_list:
        list_box.insert(tk.END, task)


def handle_add():
    """Logic for adding an item"""
    addition = entry_task.get().strip()
    if not addition:
        messagebox.showwarning("Empty Input", "Please type something to add to the list.")
        return

    task_list.append(addition)
    entry_task.delete(0, tk.END)  # Clear input box
    update_display()
    label_status.config(text=f"Added: '{addition}'", fg="#06d6a0")


def handle_remove():
    """Logic for removing an item based on list index/selection"""
    # Check if the list is empty first
    if not task_list:
        messagebox.showinfo("List Empty", "The list is empty, please add something if you want to remove.")
        label_status.config(text="The list is empty, please add something if you want to remove.", fg="#ffd166")
        return

    # Get the selected item from the GUI window list
    try:
        selected_index = list_box.curselection()[0]
    except IndexError:
        messagebox.showwarning("No Selection", "Please click/select an item from the list below to remove it.")
        return

    # Process the removal safely using the index
    if 0 <= selected_index < len(task_list):
        removed = task_list.pop(selected_index)
        update_display()
        label_status.config(text=f"Removed: {removed}", fg="#ff595e")
    else:
        # Fallback security message matching your original boundary logic
        messagebox.showerror("Error", "Please enter a number that is on the list.")


def handle_exit():
    """Logic for exiting the application"""
    label_status.config(text="Goodbye!", fg="#ffd166")
    window.after(800, window.destroy)  # Briefly pause to show goodbye, then close


# ==========================================
# GUI LAYOUT DESIGN
# ==========================================

# Main Window Configuration
window = tk.Tk()
window.title("AI Task Manager")
window.geometry("450x550")
window.configure(bg="#1e1e24")

# Styling Layout Constants
BG_MAIN = "#1e1e24"
BG_SURFACE = "#2a2a32"
BG_LIST = "#121214"
TEXT_MAIN = "#e3e3e6"
TEXT_MUTED = "#8a8a93"
ACCENT_BLUE = "#3a86ff"
ACCENT_RED = "#ff595e"

# Title Header
header = tk.Label(window, text="TASK LIST MANAGER", font=("Segoe UI", 14, "bold"), bg=BG_MAIN, fg=TEXT_MAIN)
header.pack(pady=(20, 10))

# Interactive Text Entry Label
lbl_prompt = tk.Label(window, text="What would you like to add to the list?", font=("Segoe UI", 10), bg=BG_MAIN,
                      fg=TEXT_MUTED)
lbl_prompt.pack(anchor=tk.W, padx=35, pady=(10, 2))

# Text Input Bar Field
entry_task = tk.Entry(window, font=("Segoe UI", 12), bg=BG_SURFACE, fg=TEXT_MAIN, bd=0, highlightthickness=1,
                      highlightbackground="#3d3d4a", insertbackground=TEXT_MAIN)
entry_task.pack(fill=tk.X, padx=35, ipady=8)
entry_task.focus()

# Bind Enter key to instantly execute handle_add
entry_task.bind("<Return>", lambda event: handle_add())

# Action Utility Buttons Frame
btn_frame = tk.Frame(window, bg=BG_MAIN)
btn_frame.pack(fill=tk.X, padx=35, pady=15)

# ADD button
add_btn = tk.Button(btn_frame, text="ADD TASK", font=("Segoe UI", 10, "bold"), bg=ACCENT_BLUE, fg="white", bd=0,
                    width=12, command=handle_add, cursor="hand2")
add_btn.pack(side=tk.LEFT, ipady=6, expand=True, fill=tk.X, padx=(0, 5))

# REMOVE button
remove_btn = tk.Button(btn_frame, text="REMOVE SELECTED", font=("Segoe UI", 10, "bold"), bg=ACCENT_RED, fg="white",
                       bd=0, width=16, command=handle_remove, cursor="hand2")
remove_btn.pack(side=tk.LEFT, ipady=6, expand=True, fill=tk.X, padx=(5, 5))

# EXIT button
exit_btn = tk.Button(btn_frame, text="EXIT", font=("Segoe UI", 10, "bold"), bg="#4a4a5a", fg="white", bd=0, width=8,
                     command=handle_exit, cursor="hand2")
exit_btn.pack(side=tk.LEFT, ipady=6, expand=True, fill=tk.X, padx=(5, 0))

# List Header subtitle
lbl_list_title = tk.Label(window, text="Your Current Tasks (Click an item to select it for removal):",
                          font=("Segoe UI", 9, "italic"), bg=BG_MAIN, fg=TEXT_MUTED)
lbl_list_title.pack(anchor=tk.W, padx=35, pady=(10, 2))

# Visual Scrolling List Frame
list_container = tk.Frame(window, bg=BG_MAIN)
list_container.pack(fill=tk.BOTH, expand=True, padx=35, pady=(0, 15))

# Tkinter Listbox Component
list_box = tk.Listbox(list_container, font=("Segoe UI", 11), bg=BG_LIST, fg=TEXT_MAIN, bd=0, highlightthickness=1,
                      highlightbackground="#2d2d35", selectbackground=ACCENT_BLUE, selectforeground="white",
                      activestyle="none")
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Custom Bottom Notification Bar Stream
label_status = tk.Label(window, text="App initialized. Welcome!", font=("Segoe UI", 10), bg=BG_MAIN, fg=TEXT_MUTED,
                        wraplength=380)
label_status.pack(pady=(0, 20))

window.mainloop()
