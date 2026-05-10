dark_door_scene = [

    #inspect door
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The stone door looms over the chamber."
            },
            {
                "speaker": "Narration",
                "text": "Its surface is carved into the image of a towering citadel."
            },
            {
                "speaker": "Narration",
                "text": "At the top of the engraving rests a castle crowned in shadow"
            },
            {
                "speaker": "Narration",
                "text": "Below it stands a robed figure."
            },
            {
                "speaker": "Narration",
                "text": "Its arm is raised, holding a bell above its head"
            },
        ]
    },

    #party reactions
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Rio",
                "text": "That carving feels wrong."
            },
            {
                "speaker": "Rio",
                "text": "Like it's staring back."
            },
            {
                "speaker": "Yohan",
                "text": "This place clearly revolves around that bell."
            },
            {
                "speaker": "Carmen",
                "text": "...it looks like mine."
            }
        ]
    },

    #return
    {
        "type": "transition",
        "target_scene": "dark_hub_menu"
    }
]