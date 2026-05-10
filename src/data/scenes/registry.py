
"""
Central scene registry.

Maps scene IDs to scene data so the EngineController
can transition scenes dynamically.
"""
# Intro to fork
from data.scenes.intro_to_fork.forest_intro import forest_intro_scene
from data.scenes.intro_to_fork.forest_bell import forest_bell_scene
from data.scenes.intro_to_fork.cave_fall import cave_fall_scene
from data.scenes.intro_to_fork.deep_tunnel import  deep_tunnel_scene
from data.scenes.intro_to_fork.bell_anomaly import bell_anomaly_scene
from data.scenes.intro_to_fork.fork_in_tunnel import fork_in_tunnel_scene

# fighter/temple of sight
from data.scenes.fighter.fighter_intro import fighter_intro_scene
from data.scenes.fighter.fighter_sight_hub import fighter_sight_hub_scene
from data.scenes.fighter.fighter_sight_hub_menu import fighter_sight_hub_menu_scene
from data.scenes.fighter.fighter_sight_pedestal import fighter_sight_pedestal_scene
from data.scenes.fighter.fighter_sight_door import fighter_sight_door_scene
from data.scenes.fighter.fighter_sight_bell import fighter_sight_bell_scene
from data.scenes.fighter.fighter_sight_open import fighter_sight_open_scene
from data.scenes.fighter.fighter_sight_leave import fighter_sight_leave_scene

# mage/ temple of spirit
from data.scenes.mage.mage_intro import mage_intro_scene
from data.scenes.mage.mage_spirit_hub import mage_spirit_hub_scene
from data.scenes.mage.mage_spirit_hub_menu import mage_spirit_hub_menu_scene
from data.scenes.mage.mage_spirit_pedestal import mage_spirit_pedestal_scene
from data.scenes.mage.mage_spirit_door import mage_spirit_door_scene
from data.scenes.mage.mage_spirit_bell import mage_spirit_bell_scene
from data.scenes.mage.mage_spirit_open import mage_spirit_open_scene
from data.scenes.mage.mage_spirit_leave import mage_spirit_leave_scene

# dark/temple of Dark
from data.scenes.dark.dark_intro import dark_intro_scene
from data.scenes.dark.dark_bell import dark_bell_scene
from data.scenes.dark.dark_choice import dark_choice_scene
from data.scenes.dark.dark_hub import dark_hub_scene
from data.scenes.dark.dark_hub_menu import dark_hub_menu_scene

SCENE_REGISTRY = {
    # intro to fork
    "forest_intro": forest_intro_scene,
    "forest_bell": forest_bell_scene,
    "cave_fall": cave_fall_scene,
    "deep_tunnel": deep_tunnel_scene,
    "bell_anomaly": bell_anomaly_scene,
    "fork_in_tunnel": fork_in_tunnel_scene,

    # fighter path
    "fighter_intro": fighter_intro_scene,
    "fighter_sight_hub": fighter_sight_hub_scene,
    "fighter_sight_hub_menu": fighter_sight_hub_menu_scene,
    "fighter_sight_pedestal": fighter_sight_pedestal_scene,
    "fighter_sight_door": fighter_sight_door_scene,
    "fighter_sight_bell": fighter_sight_bell_scene,
    "fighter_sight_open": fighter_sight_open_scene,
    "fighter_sight_leave": fighter_sight_leave_scene,

    # mage path
    "mage_intro": mage_intro_scene,
    "mage_spirit_hub": mage_spirit_hub_scene,
    "mage_spirit_hub_menu": mage_spirit_hub_menu_scene,
    "mage_spirit_pedestal": mage_spirit_pedestal_scene,
    "mage_spirit_door": mage_spirit_door_scene,
    "mage_spirit_bell": mage_spirit_bell_scene,
    "mage_spirit_open": mage_spirit_open_scene,
    "mage_spirit_leave": mage_spirit_leave_scene,

    # dark path
    "dark_intro": dark_intro_scene,
    "dark_bell": dark_bell_scene,
    "dark_choice": dark_choice_scene,
    "dark_hub": dark_hub_scene,
    "dark_hub_menu": dark_hub_menu_scene
}