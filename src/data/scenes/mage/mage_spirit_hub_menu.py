mage_spirit_hub_menu_scene = [
       {
        "type": "background",
        "image": "temple.jpg"
    },

    #if player has the spirit bell show all four choices
    {
        "type": "conditional",
        "if": {
            "has_spirit_bell": True
        },
        "true": [
            {
                "type": "choice",
                "options": [
                    {
                        "text": "Investigate the pedestal",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_pedestal"
                        }
                    },
                    {
                        "text": "Investigate the door",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_door"
                        }
                    },
                    {
                        "text": "Ring the Bell",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_bell"
                        }
                    },
                    {
                        "text": "Leave up the stairs",
                        "result": {
                            "action": "change_scene",
                            "target": "mage_spirit_leave"
                        }
                    }
                ]
            }
        ]
    },

    # default if no bell
    {
        "type": "choice",
        "options": [
            {
                "text": "Investigate the pedestal",
                "result": {
                    "action": "change_scene",
                    "target": "mage_spirit_pedestal"
                    }
            },
            {
                "text": "Investigate the door",
                "result": {
                    "action": "change_scene",
                    "target": "mage_spirit_door"
                    }
            },
            {
                "text": "Leave up the stairs",
                "result": {
                        "action": "change_scene",
                        "target": "mage_spirit_leave"
                    }
                }
            ]
    }
]
