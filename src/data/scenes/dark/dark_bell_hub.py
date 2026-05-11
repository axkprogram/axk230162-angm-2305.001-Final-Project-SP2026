dark_bell_hub_scene = [

      {
        "type": "background",
        "image": "temple.jpg"
    },


    #Carmen rings the bell
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen raises the broken bell slowly."
            },
            {
                "speaker": "Narration",
                "text": "The chamber falls completely silent."
            },
            {
                "speaker": "Narration",
                "text": "Then Carmen rings it."
            },
            {
                "speaker": "Narration",
                "text": "Its cold tone settles into the stone."
            }
        ]
    },

    #fail path
    {
        "type": "conditional",
        "if": {
            "dark_pedestal_complete": False
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Nothing happens."
                    },
                    {
                        "speaker": "Rio",
                        "text": "...that's it?"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "The temple rejected it."
                    },
                    {
                        "speaker": "Carmen",
                        "text": "Then something is still missing."
                    }
                ]
            },
            {
                "type": "transition",
                "target_scene": "dark_hub_menu"
            }
        ]
    },

    #success path
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
                        "text": "The pedestal answers first."
                    },
                    {
                        "speaker": "Narration",
                        "text": "The object pulses with dark light."
                    },
                    {
                        "speaker": "Narration",
                        "text": "The chamber trembles violently."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Beyond it waits a star-filled abyss."
                    }
                ]
            },
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "That is absolutely terrifying."
                    },
                    {
                        "speaker": "Rio",
                        "text": "...which means I kind of want to go in."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "We may find more of those creatures."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "But I can't ignore this."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Carmen wonders if their lost friend could be lost in this abyss."
                    }
                ]
            },

            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The temple rumbles again."
                    },
                    {
                        "speaker": "Narration",
                        "text": "It acknowledges Carmen."
                    },
                    {
                        "speaker": "Narration",
                        "text": "It wants Carmen."
                    }
                ]
            },
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The three look at one another."
                    },
                    {
                        "speaker": "Narration",
                        "text": "No one speaks."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Then together. they step into the abyss."
                    },
                    {
                        "speaker": "System",
                        "text": "Chapter End."
                    },
                    {
                        "speaker": "System",
                        "text": "Press Esc to quit"
                    }
                ]
            }
        ]
    }
]