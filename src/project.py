# testing

from engine.game_loop import GameLoop

def initialize_game():
    return GameLoop()

def display_title():
    print("Launching Minimum Playable Slice...")

def start_game(game):
    game.run()

def cleanup():
    print("Game closed.")

def main():
    display_title()
    
    game = initialize_game()

    try:
        start_game(game)
    finally:
        cleanup()

if __name__ == "__main__":
    main()