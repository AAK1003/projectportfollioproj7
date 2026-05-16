import tkinter as tk
from tkinter import messagebox

# ==========================================
# YOUR EXACT LOGIC (Adapted for GUI State)
# ==========================================

def handle_calculate():
    """Triggers the calculation workflow when the button is clicked"""
    
    # 1. Logic check for Number 1
    val1 = entry_num1.get().strip()
    if not val1.isnumeric():
        messagebox.showerror("Invalid Input", "Invalid number, please respond again to the first number.")
        return
    num1 = int(val1)
    
    # 2. Logic check for Number 2
    val2 = entry_num2.get().strip()
    if not val2.isnumeric():
        messagebox.showerror("Invalid Input", "Invalid number, please respond again to the second number.")
        return
    num2 = int(val2)
    
    # 3. Logic check for the Operation Sign
    sign = entry_sign.get().strip()
    if sign not in ['+', '-', '*', '/']:
        messagebox.showerror("Invalid Operation", "Invalid operation, please respond again.\nUse only: +, -, *, /")
        return

    # 4. Core calculation execution
    if sign == '+':
        result_text = 'The sum is: ' + str(num1 + num2)
    elif sign == '-':
        result_text = 'The difference is: ' + str(num1 - num2)
    elif sign == '*':
        result_text = 'The product is: ' + str(num1 * num2)
    elif sign == '/':
        if num2 == 0:
            result_text = 'The quotient is: Undefined'
        else:
            result_text = 'The quotient is: ' + str(num1 / num2)
            
    # Display output back to the interface
    label_result.config(text=result_text, fg="#06d6a0")

# ==========================================
# GUI LAYOUT DESIGN
# ==========================================

# Window Configuration
window = tk.Tk()
window.title("Python GUI Calculator")
window.geometry("450x450")
window.configure(bg="#1e1e24")

# Styling Constants
BG_MAIN = "#1e1e24"
BG_SURFACE = "#2a2a32"
TEXT_MAIN = "#e3e3e6"
TEXT_MUTED = "#8a8a93"
ACCENT_BLUE = "#3a86ff"

# Header Label
header = tk.Label(window, text="VISUAL CALCULATOR", font=("Segoe UI", 14, "bold"), bg=BG_MAIN, fg=TEXT_MAIN)
header.pack(pady=(20, 15))

# --- Entry Field 1 ---
lbl_num1_desc = tk.Label(
    window, 
    text="What is the first number you want to calculate with?\n(in 1+2=3, 1 would be first number)", 
    font=("Segoe UI", 9), justify=tk.LEFT, bg=BG_MAIN, fg=TEXT_MUTED
)
lbl_num1_desc.pack(anchor=tk.W, padx=30, pady=(10, 2))

entry_num1 = tk.Entry(window, font=("Segoe UI", 12), bg=BG_SURFACE, fg=TEXT_MAIN, bd=0, highlightthickness=1, highlightbackground="#3d3d4a", insertbackground=TEXT_MAIN)
entry_num1.pack(fill=tk.X, padx=30, ipady=6)

# --- Entry Field 2 ---
lbl_num2_desc = tk.Label(
    window, 
    text="What is the second number you want to calculate with?\n(in 1+2=3, 2 would be the second number)", 
    font=("Segoe UI", 9), justify=tk.LEFT, bg=BG_MAIN, fg=TEXT_MUTED
)
lbl_num2_desc.pack(anchor=tk.W, padx=30, pady=(10, 2))

entry_num2 = tk.Entry(window, font=("Segoe UI", 12), bg=BG_SURFACE, fg=TEXT_MAIN, bd=0, highlightthickness=1, highlightbackground="#3d3d4a", insertbackground=TEXT_MAIN)
entry_num2.pack(fill=tk.X, padx=30, ipady=6)

# --- Operation Sign Entry Field ---
lbl_sign_desc = tk.Label(
    window, 
    text="What is the operation you want to use on the numbers(+, -, *, /)?", 
    font=("Segoe UI", 9), bg=BG_MAIN, fg=TEXT_MUTED
)
lbl_sign_desc.pack(anchor=tk.W, padx=30, pady=(10, 2))

entry_sign = tk.Entry(window, font=("Segoe UI", 12), width=10, bg=BG_SURFACE, fg=TEXT_MAIN, bd=0, highlightthickness=1, highlightbackground="#3d3d4a", insertbackground=TEXT_MAIN)
entry_sign.pack(anchor=tk.W, padx=30, ipady=6)

# --- Calculation Trigger Action Button ---
calculate_btn = tk.Button(
    window, 
    text="CALCULATE", 
    font=("Segoe UI", 10, "bold"), 
    bg=ACCENT_BLUE, 
    fg="white", 
    bd=0, 
    command=handle_calculate, 
    activebackground="#2a6ed2", 
    activeforeground="white",
    cursor="hand2"
)
calculate_btn.pack(fill=tk.X, padx=30, pady=25, ipady=8)

# --- Result Output Display Window ---
label_result = tk.Label(window, text="The result will show here", font=("Segoe UI", 12, "bold"), bg=BG_MAIN, fg=TEXT_MUTED)
label_result.pack(pady=5)

window.mainloop()
