import random
import tkinter as tk
from tkinter import messagebox

# Word bank built into the code
WORDS = [
    "sunrise", "planet", "echo", "quantum", "delta", "fusion", "matrix", "shadow",
    "nebula", "crystal", "titanium", "galaxy", "storm", "velocity", "breeze",
    "cosmos", "signal", "flare", "aurora", "nova", "spark", "horizon", "lunar"
]

def generate_password(num_words=4, include_numbers=True, include_symbols=True):
    chosen = random.sample(WORDS, num_words)
    password = "-".join(chosen)

    if include_numbers:
        password += str(random.randint(10, 99))

    if include_symbols:
        password += random.choice("!@#$%^&*?")

    return password

def on_generate():
    try:
        num_words = int(word_entry.get())
        include_numbers = num_var.get()
        include_symbols = sym_var.get()

        password = generate_password(num_words, include_numbers, include_symbols)
        output_var.set(password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of words.")

def on_copy():
    password = output_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x320")
root.configure(bg="black")

# Common style
FONT = ("Consolas", 12, "bold")
FG_COLOR = "#c084fc"   # light purple
BG_COLOR = "black"
BTN_COLOR = "#9333ea"  # deep purple
ENTRY_COLOR = "#1e1b29"

# Input: number of words
tk.Label(root, text="Enter number of words:", font=FONT, fg=FG_COLOR, bg=BG_COLOR).pack(pady=5)
word_entry = tk.Entry(root, font=FONT, bg=ENTRY_COLOR, fg="white", insertbackground="white", justify="center")
word_entry.insert(0, "4")
word_entry.pack(pady=5)

# Checkboxes
num_var = tk.BooleanVar(value=True)
sym_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include numbers", variable=num_var, font=FONT, fg=FG_COLOR,
               bg=BG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR).pack()
tk.Checkbutton(root, text="Include symbols", variable=sym_var, font=FONT, fg=FG_COLOR,
               bg=BG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR).pack()

# Generate button
tk.Button(root, text="Generate Password", font=FONT, fg="white", bg=BTN_COLOR,
          activebackground=FG_COLOR, activeforeground="black", command=on_generate).pack(pady=10)

# Output field
output_var = tk.StringVar()
output_entry = tk.Entry(root, textvariable=output_var, font=FONT, bg=ENTRY_COLOR,
                        fg=FG_COLOR, justify="center", width=40, relief="flat")
output_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=FONT, fg="white", bg=BTN_COLOR,
          activebackground=FG_COLOR, activeforeground="black", command=on_copy).pack(pady=10)

root.mainloop()
