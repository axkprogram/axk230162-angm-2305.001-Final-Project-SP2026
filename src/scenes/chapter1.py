def start_scene(dialogue, choice):
    dialogue.start("You fall into a cave...")

    return [
        ("Follow Fighter", "fighter_path"),
        ("Follow Mage", "mage_path"), 
        ("Take Dark Path", "player_path")
    ]