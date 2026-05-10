fighter_sight_pedestal_scene = [
    
    #pedestal  desc
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The pedestal stands at the center of the chamber, older than the surrounding stone."
            },
            {
                "speaker": "Narration",
                "text": "Its surface is smooth, but a shallow compartment has been carved into its center."
            },
            {
                "speaker": "Yohan",
                "text": "A receptacle. Something's supposed to placed here."
            },
            {
                "speaker": "Rio",
                "text": "Do we have something that can go in it?"
            }
        ]
    },

    # if player has talisman
    {
        "type": "conditional",
        "if": {
            "has_talisman_of_sight": True
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Place the Talisman of Sight",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_open"
                        }
                    },
                    {
                        "text": "Leave the pedestal alone",
                        "result": {
                            "action": "change_scene",
                            "target": "fighter_sight_hub_menu"
                        }
                    }
                ]
            }
        ]
    },

    # default if player doesn't have talisman
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "We don't have anything that fits here."
            },
            {
                "speaker": "Yohan",
                "text": "Then we should keep looking."
            }
        ]
    },

    {
        "type": "transition",
        "target_scene": "fighter_sight_hub_menu"
    }
]