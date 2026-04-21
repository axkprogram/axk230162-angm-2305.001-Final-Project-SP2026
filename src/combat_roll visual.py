import random
import tkinter as tk
import combat_roll

# GUI set up
root = tk.Tk()
root.title("Roll for Strength")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# UI elements
outcome_text = canvas.create_text(150, 30, text="", font=("Arial", 16, "bold"))
dice_text = canvas.create_text(150, 150, text="20", font=("Arial", 48, "bold"))

rolling = False

# animation loop
def update_dice():
    if rolling:
        fake_roll = random.randint(1,20)
        canvas.itemconfig(dice_text, text=str(fake_roll))
        root.after(50, update_dice)

#stop animation
def stop_roll():
    global rolling
    rolling = False

    roll, damage = combat_roll.roll_damage()

    canvas.itemconfig(dice_text, text=str(roll))
    canvas.itemconfig(outcome_text, text=f"Damage: {damage}")


# start animation
def roll_animation():
    global rolling
    rolling = True

    canvas.itemconfig(outcome_text, text="Rolling damage...")

    update_dice()

    root.after(1500, stop_roll)

# button
btn = tk.Button(root, text="Attack!", command=roll_animation, font=("Arial", 14))
btn.pack(pady=10)

root.mainloop()
