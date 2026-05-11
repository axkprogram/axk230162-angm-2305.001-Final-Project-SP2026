fighter_sight_hub_menu_scene = [
    # Conditional Hub options

       {
        "type": "background",
        "image": "temple.jpg"
    },
    {
        "type": "conditional",
        "if": {
            "has_hound_bell": True
        },
        "true": [

            {
                "type": "choice",
                "options": [
                    {
                        "text": "Investigate the pedestal",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_pedestal"
                        }
                    },
                    {
                        "text": "Investigate the door",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_door"
                        }
                    },
                    {
                        "text": "Ring the Hound Bell",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_bell"
                        }
                    },
                    {
                        "text": "Leave up the stairs",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_leave"
                        }
                    }
                ]
            }
        ]
    },

    # default no bell
    {
        "type": "choice",
        "options": [
            {
                "text": "Investigate the pedestal",
                "result": {
                    "action": "change_scene",
                    "target": "fighter_sight_pedestal"
                }
            },
            {
                "text": "Investigate the door",
                "result": {
                    "action": "change_scene",
                    "target": "fighter_sight_door"
                }
            },
            {
                "text": "Leave up the stairs",
                "result": {
                    "action": "change_scene",
                    "target": "fighter_sight_leave"
                }
            }
        ]
    }
]