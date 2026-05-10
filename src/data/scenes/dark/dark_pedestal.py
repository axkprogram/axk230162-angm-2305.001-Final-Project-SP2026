dark_pedestal_scene = [

    #pedestal description
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The pedestal stands in the exact center of the chamber."
            },
            {
                "speaker": "Narration",
                "text": "A shallow compartment has been carved into its surface."
            },
            {
                "speaker": "Carmen",
                "text": "Something belongs here."
            },
            {
                "speaker": "Rio",
                "text": "Probably the creepy object."
            }
        ]
    },

    #if not placed yet
    {
        "type": "conditional",
        "if": {
            "dark_pedestal_complete": False
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Leave the pedestal alone",
                        "result": {
                            "action": "change_scene",
                            "target": "dark_hub_menu"
                        }
                    }
                ]
            }
        ]
    },

    # after placing 
    {
        "type": "conditional",
        "if": {
            "dark_pedestal_complete": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Carmen places the object into the compartment."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Nothing happens."
                    },
                    {
                        "speaker": "Rio",
                        "text": "...that's disappointing."
                    }
                ]
            },
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Try to remove the object",
                        "result": {
                            "action": "change_scene",
                            "target": "dark_pedestal_locked"
                        }
                    },
                    {
                        "text": "Leave it there",
                        "result": {
                            "action": "change_scene",
                            "target": "dark_hub_menu"
                        }
                    }
                ]
            }
        ]
    }
]