mage_spirit_door_scene = [

    # door desc
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The stone door towers above the party."
            },
            {
                "speaker": "Narration",
                "text": "A specter is carved into its surface, surrounded by blue flames."
            },
            {
                "speaker": "Narration",
                "text": "At the center of its chest is an empty circular socket."
            },
            {
                "speaker": "Yohan",
                "text": "Its core is missing."
            },
            {
                "speaker": "Rio",
                "text": "Which means we're probably carrying the key"
            }
        ]
    },

    # player has gemstone
    {
        "type": "conditional",
        "if": {
            "has_spirit_gem": True
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Place the blue gemstone into the missing core",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_open"
                        }
                    },
                    {
                        "text": "Leave the door alone",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_hub_menu"
                        }
                    }
                ]
            }
        ]
    },

    # default if no gemstone
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "We don't have what belongs here."
            },
            {
                "speaker": "Yohan",
                "text": "Then we keep searching."
            }
        ]
    },
    {
        "type": "transition",
        "target_scene": "mage_spirit_hub_menu"
    }
]