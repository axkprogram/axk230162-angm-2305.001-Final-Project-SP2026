mage_spirit_pedestal_scene = [

    # pedestal description
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The pedestal stands at the center of the chamber, worn smooth by time."
            },
            {
                "speaker": "Narration",
                "text": "A circular compartment has been carved into its center."
            },
            {
                "speaker": "Yohan",
                "text": "This wasn't decorative. Somehitng belongs here."
            },
            {
                "speaker": "Rio",
                "text": "Well do we have anything?"
            }
        ]
    },

    # player has talisman
    {
        "type": "conditional",
        "if": {
            "has_spirit_talisman": True
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Place the Talisman of Spirit",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_open"
                        }
                    },
                    {
                        "text": "Leave the pedestal alone",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_hub_menu"
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
                "text": "We don't have anything that fits."
            },
            {
                "speaker": "Yohan",
                "text": "Then our answer must be elsewhere."
            }
        ]
    },

    #transition
    {
        "type": "transition",
        "target_scene": "mage_spirit_hub_menu"
    }
]