
"""
Central scene registry.

Maps scene IDs to scene data so the EngineController
can transition scenes dynamically.
"""
from data.scenes.forest_intro import forest_intro_scene
from data.scenes.forest_bell import forest_bell_scene
from data.scenes.cave_fall import cave_fall_scene
from data.scenes.deep_tunnel import  deep_tunnel_scene
from data.scenes.bell_anomaly import bell_anomaly_scene
from data.scenes.fork_in_tunnel import fork_in_tunnel_scene

SCENE_REGISTRY = {
    "forest_intro": forest_intro_scene,
    "forest_bell": forest_bell_scene,
    "cave_fall": cave_fall_scene,
    "deep_tunnel": deep_tunnel_scene,
    "bell_anomaly": bell_anomaly_scene,
    "fork_in_tunnel": fork_in_tunnel_scene
}