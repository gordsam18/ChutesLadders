import tkinter as tk
import random

def on_click():
    roll = random.randint(1,6)
    rollLabel.config(text=f"You rolled a {roll}")
    print(roll)

root = tk.Tk()
currentPlayerLabel= tk.Label(
    root,
    text="Player 1"
)
currentPlayerLabel.pack()


button = tk.Button(root, 
                   text="Roll", 
                   command=on_click, 
                   #bg="blue", 
                   #fg="white", 
                   font=("Arial", 14),
                   width=10,
                   height=2)
button.pack(pady=10)

rollLabel = tk.Label(
    root,
    text=""
)
rollLabel.pack()

root.mainloop()