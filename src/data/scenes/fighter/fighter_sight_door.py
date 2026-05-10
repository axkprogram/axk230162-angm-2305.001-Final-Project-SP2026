fighter_sight_door_scene = [

    # inspect the door
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The stone door towers over the chamber."
            },
            {
                "speaker": "Narration",
                "text": "A hound with many carved eyes is engraved into its center."
            },
            {
                "speaker": "Narration", 
                "text": "One eye socket is empty."
            },
            {
                "speaker": "Yohan",
                "text": "Something is clearly meant to be inserted there."
            },
            {
                "speaker": "Rio",
                "text": "Strange kind of lock."
            }
        ]
    },

    # if has gemstone
    {
        "type": "conditional",
        "if": {
            "has_hound_gem": True
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Place the red gemstone in the missing eye",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_open"
                        }
                    },
                    {
                        "text": "Leave the door alone",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_hub"
                        }
                    }
                ]
            }
        ]
    },

    # no gemstone
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "We don't have whatever this needs."
            },
            {
                "speaker": "Yohan",
                "text": "Then forcing it would be pointless."
            }
        ]
    },

    {
        "type": "transition",
        "target_scene": "fighter_sight_hub"
    }
]