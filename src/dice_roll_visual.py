import random
import tkinter as tk
import roll_for_luck_dice

# GUI set up
root = tk.Tk()
root.title("Roll for Fortune")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# text elements
outcome_text = canvas.create_text(150, 30, text="", font=("Arial", 16, "bold"))
dice_text = canvas.create_text(150, 150, text="20", font=("Arial", 48, "bold"))

rolling = False