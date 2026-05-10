dark_intro_scene = [

    # opening dialogue
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen takes the lead down the center path"
            },
            {
                "speaker": "Carmen",
                "text": "The air feels heavy here."
            },
            {
                "speaker": "Carmen",
                "text": "Like the cave itself is pressing down on us."
            },
            {
                "speaker": "Rio",
                "text": "...comforting"
            },
            {
                "speaker": "Yohan",
                "text": "The noblewoman may want proof this temple exists, but I don't think she wants us to die here."
            }
        ]
    },

    #darkness conversation
    {
        "types": "dialogue",
        "lines": [
            {
                "speaker": "Yohan",
                "text": "Even with magic light, this tunnel is unnaturally dark."
            },
            {
                "speaker": "Rio",
                "text": "Then maybe I should lead."
            },
            {
                "speaker": "Rio",
                "text": "I don't trust this place."
            },
            {
                "speaker": "What if this cave is the temple?"
            },
            {
                "speaker": "Narration",
                "text": "Rio and Yohan both fall silent."
            },
            {
                "speaker": "Yohan",
                "text": "Let's hope its not"
            },
            {
                "speaker": "Rio",
                "text": "But if it is... I don't like the idea of it wanting us here."
            }
        ]
    },

    # internal thoughts
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen doesn't think this is the temple."
            },
            {
                "speaker": "Narration",
                "text": "But whatever they're looking for feels very close."
            }
        ]
    },

    # monster appears
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen suddenly raises an arm, stopping Yohan and Rio."
            },
            {
                "speaker": "Carmen",
                "text": "Stay behind me."
            },
            {
                "speaker": "Narration",
                "text": "Something moves in the darkness ahead."
            },
            {
                "speaker": "Narration",
                "text": "A strange creature approaches...something none of them have ever seen before."
            },
            {
                "speaker": "Yohan",
                "text": "I've never seen anything like it. Not even in the Tower records."
            },
            {
                "speaker": "Rio",
                "text": "I don't like the look of that thing."
            },
            {
                "speaker": "Carmen",
                "text": "I'll take care of it."
            }
        ]
    },

    # battle
    {
        "type": "battle",
        "player": "CARMEN",
        "enemy": "MONSTER"
    },

    # after special battle trigger
    {
        "type": "transition",
        "target_scene": "dark_bell"
    }
]