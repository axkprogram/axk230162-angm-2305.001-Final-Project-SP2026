import pygame

from engine.controller import EngineController
from state.game_state import GameState
from scene.scene_manager import SceneManager
from data.scenes.registry import SCENE_REGISTRY
from battle.battle_manager import BattleManager

# screen constants
WIDTH = 1280
HEIGHT = 720
FPS = 60

class GameLoop:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minimum Playable Slice VN")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)

       #place holder assests
        self.backgrounds = {
            "forest.jpg": self.load_image("assets/bg/forest.jpg", (WIDTH, HEIGHT)),
            "cave_fall.jpg": self.load_image("assets/bg/cave_fall.jpg", (WIDTH, HEIGHT)),
            "cave_tunnel.jpg": self.load_image("assets/bg/cave_tunnel.jpg", (WIDTH, HEIGHT)),
            "fork_in_tunnel.jpg": self.load_image("assets/bg/fork_in_tunnel.jpg", (WIDTH, HEIGHT)),
            "temple.jpg": self.load_image("assets/bg/temple.jpg", (WIDTH, HEIGHT))
        }

        print("BG:", self.backgrounds)

        self.left_portrait = self.load_image(
            "assets/chars/yohan.jpg",
            (400, 600)
        )

        self.right_portrait = self.load_image(
            "assets/chars/rio.jpg",
            (400, 600)
        )
        #portrait debug
        print("BG:", self.background)
        print("LEFT:", self.left_portrait)
        print("RIGHT:", self.right_portrait)

        # systems
        self.game_state = GameState()

        self.scene_manager = SceneManager()

        self.controller = EngineController(
            self.game_state
            )

        self.controller.register_scene_system(
            self.scene_manager
            )

        self.scene_manager.load_scene(
            SCENE_REGISTRY["forest_intro"]
            )
       
        # load first dialogue immediately
        self.controller.update({})

        

        #battle registration
        self.battle = BattleManager()
        self.controller.register_battle_system(self.battle)

    # Input
    def handle_input(self):
        input_data = {}

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.controller.running = False

            elif event.type == pygame.KEYDOWN:

                ui = self.controller.ui_state

                # always allow quit
                if event.key == pygame.K_ESCAPE:
                    self.controller.running = False

                # Battle
                elif ui["mode"] == "battle":

                    available_moves = []

                    for move in self.battle.player["moves"]:
                        if move.get("locked") and not self.battle.dark_special_ready:
                            continue
                        available_moves.append(move)

                    if event.key == pygame.K_1 and len(available_moves) >= 1:
                        self.battle.use_player_move(available_moves[0])

                    elif event.key == pygame.K_2 and len(available_moves) >= 2:
                        self.battle.use_player_move(available_moves[1])

                    elif event.key == pygame.K_3 and len(available_moves) >= 3:
                        self.battle.use_player_move(available_moves[2])

                    #enemy turn
                    if self.battle.active and self.battle.turn == "enemy":
                        self.battle.enemy_turn()

                    #dark path scene trigger
                    if self.battle.trigger_dark_scene:
                        self.controller.change.scene("dark_bell_scene")
                        self.battle.trigger_dark_scene = False

                    #normal battle end
                    elif not self.battle.active:
                        self.controller.ui_state["mode"] = "dialogue"
                        self.controller.update({})

                 #advance dialogue
                elif ui ["mode"] == "dialogue":

                    if event.key == pygame.K_SPACE:
                        input_data["advance"] = True

                #choices 1/2/3
                elif ui["mode"] == "choice":
                    if event.key == pygame.K_1:
                        input_data["choice_select"] = 0

                    elif event.key == pygame.K_2:
                        input_data["choice_select"] = 1

                    elif event.key == pygame.K_3:
                        input_data["choice_select"] = 2

                    elif event.key == pygame.K_4:
                        input_data["choice_select"] = 3

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.controller.ui_state["mode"] == "dialogue":
                        input_data["advance"] = True

        return input_data
    
    # text wrapping
    def wrap_text(self, text, font, max_width):

        words = text.split()
        lines = []
        current = ""

        for word in words:
            test = current + word + " "

            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "

        if current:
            lines.append(current)

        return lines
    
    #render
    def render(self):

        bg_name = self.controller.ui_state["background"]
        bg = self.backgrounds.get(bg_name)

        if bg:
            self.screen.blit(bg,(0,0))
        else:
            self.screen.fill((20, 20, 30))

        ui = self.controller.ui_state

        # character portraits
        if self.left_portrait:
            self.screen.blit(
                self.left_portrait,
                (50, 100)
            )

        if self.right_portrait:
            self.screen.blit(
                self.right_portrait,
                (830, 100)
            )

        #dialogue box
        pygame.draw.rect(
            self.screen,
            (20, 20, 20),
            (20, 500, 1240, 200)
        )

        # dialogue
        if ui["mode"] == "dialogue":

            speaker = self.small_font.render(
                ui["speaker"],
                True,
                (255, 255, 0)
            )
            self.screen.blit(speaker, (40, 520))

            wrapped = self.wrap_text(
                ui["text"],
                self.small_font,
                1100
            )

            y = 560

            for line in wrapped:
                text_surface = self.small_font.render(
                    line,
                    True,
                    (255, 255, 255)
                )
                self.screen.blit(
                    text_surface,
                    (40, y)
                )
                y += 30
        
        # choice
        elif ui["mode"] == "choice":

            y = 540

            for i, choice in enumerate(ui["choices"]):
                label = f"{i+1}. {choice['text']}"

                wrapped_choices = self.wrap_text(
                    label,
                    self.small_font,
                    1200
                )

                for line in wrapped_choices:
                    text_surface = self.small_font.render(
                        line,
                        True,
                        (255, 255, 255)
                    )

                    self.screen.blit(
                        text_surface,
                        (40, y)
                    )

                    y += 30 # line spacing

                y += 15 # extra spacing between choices

            # battle
        elif ui["mode"] == "battle":

            battle = self.controller.battle_system

            player = self.font.render(
                f"{battle.player['name']} HP: {battle.player['hp']}",
                True,
                (255,255,255)
            )
            self.screen.blit(player, (50,50))

            enemy = self.font.render(
                f"{battle.enemy['name']} HP: {battle.enemy['hp']}",
                True,
                (255,255,255)
            )
            self.screen.blit(enemy, (50,100))

            msg = self.font.render(
                battle.message, 
                True, 
                (255,255,0)
            )
            self.screen.blit(msg, (50, 10))

            y = 550

            #new
            available_moves = []

            for move in battle.player["moves"]:
                if move.get("locked") and not battle.dark_special_ready:
                    continue
                available_moves.append(move)
            
            for i, move in enumerate(available_moves):
                txt = self.small_font.render(
                    f"{i+1}. {move['name']}",
                    True,
                    (255,255,255)
                )
                self.screen.blit(txt, (50, 550 + i*30))

        pygame.display.flip()

    # load image
    def load_image(self, path, size=None):
        try:
            img = pygame.image.load(path).convert_alpha()

            if size:
                img = pygame.transform.scale(img, size)

            return img
        
        except:
            print("Missing image:", path)
            return None

    # Main Loop
    def run(self):

        while self.controller.running:

            input_data = self.handle_input()

            self.controller.update(
                input_data
            )

            self.render()

            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    GameLoop().run()