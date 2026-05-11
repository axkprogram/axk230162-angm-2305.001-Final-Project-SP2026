dark_choice_scene = [
     {
        "type": "background",
        "image": "cave_tunnel.jpg"
    },

    #introduce the object
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The statue sits motionless on the cave floor."
            },
            {
                "speaker": "Narration",
                "text": "Its thorned crown makes it look almost alive."
            },
            {
                "speaker": "Rio",
                "text": "I hate everything about that thing."
            },
            {
                "speaker": "Yohan",
                "text": "Whatever it is, we should decide what to do with it."
            }
        ]
    },

    # player choice
    {
        "type": "choice",
        "options": [
            {
                "text": "Have Yohan analyze the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_dark_talisman": True
                    }
                }
            },
            {
                "text": "Have Rio destroy the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_dark_object": True
                    }
                }
            },
            {
                "text": "Have Carmen keep the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_dark_crown": True
                    }
                }
            }
        ]
    },

    # Yohan analyze
    {
        "type": "conditional",
        "if": {
            "has_dark_talisman": True
        },
        "true": [
            {
                "type":"dialogue",
                "lines": [
                    {
                        "speaker": "Yohan",
                        "text": "It's... some kind of talisman."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "I can't get anything else out of it. Which doesn't make sense, that goes against every law of magic."
                    },
                    {
                        "speaker": "Rio",
                        "text": "So it's cursed. Great"
                    },
                    {
                        "speaker": "Narration",
                        "text": "Holding the talisman, Carmen feels like it's trying to figure them out."
                    }
                ]
            }
        ]
    },

    #Rio destroy
    {
        "type": "conditional",
        "if": {
            "has_dark_object": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Rio slams the object against stone."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Nothing happens."
                    },
                    {
                        "speaker": "Narration",
                        "text": "She tries again."
                    },
                    {
                        "speaker": "Rio",
                        "text": "Why won't this thing break?"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It's just...refusing to be destroyed."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It sounds like something is inside it."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Carmen feels like the object is trying to destroy them."
                    }
                ]
            }
        ]
    },

    # Carmen keep
    {
        "type": "conditional",
        "if": {
            "has_dark_crown": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Carmen lifts the object."
                    },
                    {
                        "speaker": "Narration",
                        "text": "It feels like nothing."
                    },
                    {
                        "speaker": "Narration",
                        "text": "And everything."
                    },
                    {
                        "speaker": "Rio",
                        "text": "That's it?"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It looks too sinister for nothing to happen."
                    },
                    {
                        "speaker": "Rio",
                        "text": "That means there's more to it."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Which makes it dangerous."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Carmen feels the object is trying to take something from them."
                    }
                ]
            }
        ]
    },

    #move to hub
    {
        "type": "transition",
        "target_scene": "dark_hub"
    }
]