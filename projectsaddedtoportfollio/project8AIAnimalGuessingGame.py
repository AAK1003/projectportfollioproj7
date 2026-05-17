import random
import tkinter as tk
from tkinter import scrolledtext
from google import genai

# 1. Initialize the Gemini Client
client = genai.Client(api_key)

# 2. Setup the Game Data (Untouched Logic)
animals = [
    "Dog", "Cat", "Elephant", "Lion", "Tiger", "Horse", "Cow", "Pig", "Monkey", "Bear",
    "Eagle", "Owl", "Penguin", "Parrot", "Crow", "Duck", "Swan",
    "Snake", "Turtle", "Crocodile", "Frog",
    "Shark", "Dolphin", "Whale", "Octopus",
    "Butterfly", "Spider", "Ant", "Bee"
]
chosen_animal = random.choice(animals)

system_instructions = f"""
    You are the host of a simple animal guessing game. 
    Your secret animal is: {chosen_animal}.
    Rules:
        - Answer the user's questions accurately based on this animal.
        - Keep answers brief (one or two sentences).
        - Do NOT reveal the name of the animal until they guess it exactly.
        - If they guess "{chosen_animal}" correctly, congratulate the player based on how many turns they took:
            - for 1-5 turns say exactly: "Good Job! You're a Master! You Won!"
            - for 6-10 turns say exactly: "Good Job! You're an Expert! You Won!"
            - for 10-20 turns say exactly: "Good Job! You're great at this! You Won!"
            - for 20+ turns say exactly: "Good Job! You Won!"
"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config={"system_instruction": system_instructions}
)

# 3. Styling Configuration Constants
BG_MAIN = "#1e1e24"  # Dark charcoal background
BG_SURFACE = "#2a2a32"  # Lighter surface color for input/containers
BG_CHAT = "#121214"  # Deep black for chat stream
TEXT_MAIN = "#e3e3e6"  # Clean white-gray text
ACCENT_BLUE = "#3a86ff"  # Vibrant modern blue for buttons
ACCENT_GREEN = "#06d6a0"  # Soft mint green for user identifiers
ACCENT_PURPLE = "#b5179e"  # Deep pink/purple for AI host identifiers


# 4. GUI Event Handling Function
def send_message(event=None):
    user_text = input_box.get().strip()

    if not user_text:
        return

    # Append User Message with Color Tags
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: ", "user_tag")
    chat_display.insert(tk.END, f"{user_text}\n\n", "main_text")

    input_box.delete(0, tk.END)

    if user_text.lower() in ["exit", "quit"]:
        chat_display.insert(tk.END, "System: ", "ai_tag")
        chat_display.insert(tk.END, f"Game over! The secret animal was the {chosen_animal}.\n\n", "main_text")
        input_box.config(state=tk.DISABLED, bg="#1a1a20")
        send_button.config(state=tk.DISABLED, bg="#4a4a5a")
        chat_display.config(state=tk.DISABLED)
        return

    try:
        ai_response = chat.send_message(user_text)

        # Append AI Message with Color Tags
        chat_display.insert(tk.END, "AI Host: ", "ai_tag")
        chat_display.insert(tk.END, f"{ai_response.text}\n\n", "main_text")

        if 'You Won' in ai_response.text:
            input_box.config(state=tk.DISABLED, bg="#1a1a20")
            send_button.config(state=tk.DISABLED, bg="#4a4a5a")
    except Exception as e:
        chat_display.insert(tk.END, f"System Error: {str(e)}\n\n", "main_text")

    chat_display.see(tk.END)
    chat_display.config(state=tk.DISABLED)


# 5. Window Frame Assembly
window = tk.Tk()
window.title("AI Animal Guessing Game")
window.geometry("520x650")
window.configure(bg=BG_MAIN)

# Main Title Header (FIXED: Removed letterspace parameter)
header = tk.Label(
    window,
    text="ANIMAL GUESSING GAME",
    font=("Segoe UI", 14, "bold"),
    bg=BG_MAIN,
    fg=TEXT_MAIN
)
header.pack(pady=(20, 10))

# Subtitle / Rule reminder
subtitle = tk.Label(
    window,
    text="Ask questions or type 'exit' to give up",
    font=("Segoe UI", 9, "italic"),
    bg=BG_MAIN,
    fg="#8a8a93"
)
subtitle.pack(pady=(0, 10))

# Scrollable Chat Log Display Terminal
chat_display = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=55,
    height=24,
    font=("Segoe UI", 11),
    bg=BG_CHAT,
    fg=TEXT_MAIN,
    bd=0,
    highlightthickness=1,
    highlightbackground="#2d2d35",
    padx=12,
    pady=12
)
chat_display.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Custom Text Formatting Colors (Tags)
chat_display.tag_config("user_tag", foreground=ACCENT_GREEN, font=("Segoe UI", 11, "bold"))
chat_display.tag_config("ai_tag", foreground=ACCENT_PURPLE, font=("Segoe UI", 11, "bold"))
chat_display.tag_config("main_text", foreground=TEXT_MAIN)

# Welcome Initialization Screen Message
chat_display.insert(tk.END, "AI Host: ", "ai_tag")
chat_display.insert(tk.END,
                    "I've selected a secret animal from my list. Start asking questions to figure out what it is!\n\n",
                    "main_text")
chat_display.config(state=tk.DISABLED)

# Lower Tray Controller Layout
bottom_frame = tk.Frame(window, bg=BG_MAIN)
bottom_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=(10, 20))

# Text Input Field
input_box = tk.Entry(
    bottom_frame,
    font=("Segoe UI", 12),
    bg=BG_SURFACE,
    fg=TEXT_MAIN,
    bd=0,
    highlightthickness=1,
    highlightbackground="#3d3d4a",
    insertbackground=TEXT_MAIN  # White blinking text cursor
)
input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 12))
input_box.focus()
input_box.bind("<Return>", send_message)

# Interactive Flat Send Button
send_button = tk.Button(
    bottom_frame,
    text="SEND",
    font=("Segoe UI", 10, "bold"),
    bg=ACCENT_BLUE,
    fg="white",
    bd=0,
    width=12,
    command=send_message,
    activebackground="#2a6ed2",
    activeforeground="white",
    cursor="hand2"
)
send_button.pack(side=tk.RIGHT, ipady=8)

window.mainloop()
