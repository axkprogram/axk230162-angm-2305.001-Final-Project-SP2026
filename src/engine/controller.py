from data.scenes.registry import SCENE_REGISTRY
from data.battle import *

class EngineController:
    """
    Minimal game controller for VN MVP.
    
    Responsibilities:
    - Receive SceneManager output
    - Update UI state
    - Maintain game state flags
    - Switch modes cleanly
    """

    def __init__(self, game_state):
        self.game_state = game_state
        self.scene_system = None
        self.running = True
        self.battle_system = None

        # what renderer reads
        self.ui_state = {
            "mode": "dialogue",
            "speaker": "",
            "text": "",
            "choices": [],
            "background": "forest.jpg"
        }

    #Register Scene Manager
    def register_scene_system(self, scene_system):
        self.scene_system = scene_system

    # Register battle manager
    def register_battle_system(self, battle_system):
        self.battle_system = battle_system

    #Main update
    def update(self, input_data):

        if self.battle_system and self.battle_system.active:
            return

        if not self.scene_system:
            return
        
        while self.running:

            result = self.scene_system.update(
                input_data,
                self.game_state
            )

            if not result:
                break

            self._handle_result(result)

            # stop so player can read dialogue or make a choice
            if result.get("action") in (
                "dialogue", 
                "choice",
                "change_scene",
                "start_battle"
            ):
                break

            # prevent held key repeating
            input_data = {}


    # result handler
    def _handle_result(self, result):

        action = result.get("action")

        #background
        if action == "background":
            print("SETTING BG:", result["image"])
            self.ui_state["background"] = result["image"]

        # dialogue
        elif action == "dialogue":

            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = result.get(
                "speaker", ""
            )
            self.ui_state["text"] = result.get(
                "text", ""
            )

            self.ui_state["choices"] = []

        # Choice
        elif action == "choice":

            self.ui_state["mode"] = "choice"
            self.ui_state["choices"] = result.get(
                "choices", []
            )

            self.ui_state["speaker"] = ""
            self.ui_state["text"] = ""

        # State Change
        elif action == "state_change":
            print(result)

            changes = result.get(
                "changes", {}
            )

            for key, value in changes.items():
                setattr(
                    self.game_state,
                    key,
                    getattr(
                        self.game_state,
                        key,
                        0
                    ) + value
                    if isinstance(value, int)
                    else value
                )
            
            # debug
            print("Route:", self.game_state.route_state)
        
        # Start battle
        elif action == "start_battle":

            print("STARTING BATTLE")

            self.ui_state["background"] = None

            players = {
                "RIO": RIO,
                "YOHAN": YOHAN,
                "CARMEN": CARMEN
            }

            enemies = {
                "HOUND": HOUND,
                "SPECTER": SPECTER,
                "MONSTER": MONSTER
            }

            self.battle_system.start_battle(
                players[result["player"]],
                enemies[result["enemy"]]
            )

            self.ui_state["mode"] = "battle"

        # Scene Change
        elif action == "change_scene":
            target = result.get("target")
            print("loading scene:", target)

            #special branch handler
            if target == "route_intro":

                if self.game_state.route_state == "fighter":
                    target = "fighter_intro"

                elif self.game_state.route_state == "mage":
                    target = "mage_intro"

                elif self.game_state.route_state == "dark":
                    target = "dark_intro"

            if target in SCENE_REGISTRY:
                self.scene_system.load_scene(
                    SCENE_REGISTRY[target]
                )

                self.game_state.current_scene_id = target

                self.update({})

                #stop and let next frame render new scene
                return
            else:
                print("SCENE NOT FOUND", target)

        # Scene End
        elif result.get("end_scene"):
            self.ui_state["mode"] = "dialogue"
            self.ui_state["speaker"] = "System"
            self.ui_state["text"] = "End of current playable build. Press ESC to quit"


    # Stop Engine
    def stop(self):
        self.running = False