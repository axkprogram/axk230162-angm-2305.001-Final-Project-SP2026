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

def update_dice():
    """Animation loop: keeps changing while rolling"""
    if rolling:
        fake_roll = random.randint(1,20)
        canvas.itemconfig(dice_text, text=str(fake_roll))
        root.after(50, update_dice)

def stop_roll():
    global rolling
    rolling = False

    roll, outcome = roll_for_luck_dice.story_roll()

    canvas.itemconfig(dice_text, text=str(roll))
    canvas.itemconfig(outcome_text, text=outcome.capitalize())

def roll_animation():
    """Start rolling animation, then settle on the final result"""
    global rolling
    rolling = True

    canvas.itemconfig(outcome_text, text="Rolling...")

    update_dice()

    # stop after 1.5 seconds
    root.after(1500, stop_roll)



# button
btn = tk.Button(root, text="Roll D20", command= roll_animation, font=("Arial", 14))
btn.pack(pady=10)

root.mainloop()