import random
from roll_for_luck_dice import story_roll
from combat_roll import roll_damage

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"{self.name} takes {dmg} damage! (HP: {self.hp})")

    def is_alive(self):
        return self.hp > 0
    
def player_turn(player, enemy):
    print("\n--- Player Turn---")

    input("Press Enter to roll for luck...")

    # Luck Roll
    roll, outcome = story_roll()
    print(f"You rolled {roll} ({outcome})")

    if roll < 8:
        print ("You hesitate...")
        return
    
    print("You attack!")

    input("Press Enter to roll for damage")

    # Damage roll
    dmg_roll, damage = roll_damage()
    print(f"Damage roll: {dmg_roll} {damage} damage")

    enemy.take_damage(damage)

def enemy_turn(enemy, player):
    print("\n--- Enemy Turn ---")

    # Enemy skips luck roll
    dmg_roll, damage = roll_damage()
    print(f"Enemy rolls {dmg_roll} {damage} damage")

    player.take_damage(damage)

def battle():
    player = Character("Player", 30)
    enemy = Character("Enemy", 25)

    while player.is_alive() and enemy.is_alive():
        player_turn(player, enemy)

        if enemy.is_alive():
            enemy_turn(enemy, player)

    # outcome

    if player.is_alive():
        print("\n You win!")
        break

    else:
        print("\n You lost..")

        # try again only after loss
        while True:
            choice = input ("Try again? (yes/no): ").lower()

            if choice in  ["yes", "y"]:
                print("Restarting battle...")
                break

            elif choice in ["no", "n"]:
                print("Game over.")
                return
            
            else:
                print("Please enter 'yes' or 'no'.")


battle()