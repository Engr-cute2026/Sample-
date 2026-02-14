import tkinter as tk
from tkinter import messagebox

def calculate_reactions():
    try:
        L = float(entry_length.get())
        P = float(entry_load.get())
        a = float(entry_distance.get())

        if a > L:
            messagebox.showerror("Input Error", "Load distance cannot exceed beam length.")
            return

        RA = P * (L - a) / L
        RB = P * a / L

        label_RA.config(text=f"Reaction at A (RA): {RA:.2f} kN")
        label_RB.config(text=f"Reaction at B (RB): {RB:.2f} kN")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


# Create window
root = tk.Tk()
root.title("Simple Beam Support Reaction Calculator")
root.geometry("350x250")

# Inputs
tk.Label(root, text="Beam Length L (m)").pack()
entry_length = tk.Entry(root)
entry_length.pack()

tk.Label(root, text="Point Load P (kN)").pack()
entry_load = tk.Entry(root)
entry_load.pack()

tk.Label(root, text="Distance from Left Support a (m)").pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

# Button
tk.Button(root, text="Calculate Reactions", command=calculate_reactions).pack(pady=10)

# Results
label_RA = tk.Label(root, text="Reaction at A (RA): ")
label_RA.pack()

label_RB = tk.Label(root, text="Reaction at B (RB): ")
label_RB.pack()

# Run app
root.mainloop()