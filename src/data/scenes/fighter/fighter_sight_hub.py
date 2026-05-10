fighter_sight_hub_scene = [

    # arrival
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The tunnel opens into a circular stone chamber."
            },
            {
                "speaker": "Narration",
                "text": "At its center, rests a pedestal with a shallow compartment."
            },
            {
                "speaker": "Narration",
                "text": "A staircase nearby appears to lead back to the surface."
            },
            {
                "speaker": "Rio",
                "text": "So this... is the end of the path."
            },
            {
                "speaker": "Yohan",
                "text": "Or just the beginning."
            }
        ]
    },

    # Conditional Hub options
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
    }
]