dark_hub_menu_scene = [
    {
        "type": "choice",
        "options": [
            {
                "text": "Investigate the pedestal",
                "result": {
                    "action": "change_scene",
                    "target": "dark_pedestal"
                }
            },
            {
                "text": "Investigate the door",
                "result": {
                    "action": "change_scene",
                    "target": "dark_pedestal"
                }
            },
            {
                "text": "Ring Carmen's bell",
                "result": {
                    "action": "change_scene",
                    "target": "dark_bell_hub"
                }
            },
            {
                "text": "Leave up the stairs",
                "result": {
                    "action": "change_scene",
                    "target": "dark_leave"
                }
            }
        ]
    }
]