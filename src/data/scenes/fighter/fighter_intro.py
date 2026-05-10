fighter_intro_scene = [
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Rio",
                "text": "I'll take the lead. Stay close.",
                "emotion": "confident"
            },
            {
                "speaker": "Yohan",
                "text": "The noblewoman asked us to find a temple, not die in a cave"
            },
            {
                "speaker": "Yohan",
                "text": "At this rate we might accomplish the latter first."
            },
            {
                "speaker": "Carmen",
                "text": "What if this cave is the temple?"
            },
            {
                "speaker": "Yohan",
                "text": "...I hadn't considered that."
            },
            {
                "speaker": "Rio",
                "text": "If that's true, we're in real danger."
            },
            {
                "speaker": "Rio",
                "text": "Which means this just got interesting."
            }
        ]
    },

    # Carmen internal thought
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen isn't convinced that this tunnel is the temple itself."
            },
            {
                "speaker": "Narration",
                "text" : "But they're certain they're getting closer to something."
            }
        ]
    },

    #enemy appears
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Rio suddenly throws an arm out, stopping Carmen and Yohan"
            },
            {
                "speaker": "Rio",
                "text": "Stop. Something's ahead."
            },
            {
                "speaker": "Narration",
                "text": "A creature emerges from the darkness."
            },
            {
                "speaker": "Narration",
                "text": "A hound. Its body is covered in far, far too many eyes. Some don't even seem to be attached to its body."
            },
            {
                "speaker": "Yohan",
                "text": "That's... wrong"
            },
            {
                "speaker": "Yohan",
                "text": "Magic won't work on it. I can feel it resisting."
            },
            {
                "speaker": "Rio",
                "text": "Good."
            },
            {
                "speaker": "Rio",
                "text": "More fun for me."
            }
        ]
    },

    # battle trigger
    {
        "type": "battle",
        "player": "RIO",
        "enemy": "HOUND"
    },

    # after battle
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The many-eyed hound collapses."
            },
            {
                "speaker": "Narration",
                "text": "Its body dissolves into ash."
            },
            {
                "speaker": "Narration",
                "text": "Something remains."
            },
            {
                "speaker": "Narration",
                "text": "A carved object depicting a sitting hound, its body covered in tiny eyes."
            },
            {
                "speaker": "Rio",
                "text": "I really hate that it left a souvenir."
            }
        ]
    },

    # artifact choice
    {
        "type": "choice",
        "options": [

            #analyze
            {
                "text": "Have Yohan analyze the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_talisman_of_sight": True
                    }
                }
            },

            #destroy
            {
                "text": "Have Rio destroy the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_hound_gem": True
                    }
                }
            },

            #keep
            {
                "text": "Have Carmen keep the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_hound_bell": True
                    }
                }
            }
        ]
    },

    #talisman path
    {
        "type": "conditional",
        "if": {
            "has_talisman_of_sight": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Yohan",
                        "text": "It's called the Talisman of Sight apparently."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Something used in old rituals. The Tower would probably know more about it..."
                    },
                    {
                        "speaker": "Rio",
                        "text": "So we keep creepy statues now?"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "It feels important."
                    }
                ]
            }
        ]
    },

    # gem path
    {
        "type": "conditional",
        "if": {
            "has_hound_gem": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Rio crushes the statue."
                    },
                    {
                        "speaker": "Narration",
                        "text": "inside is a red gemstone. Shaped like the hound's eye."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "You destroy everything interesting."
                    },
                    {
                        "speaker": "Rio",
                        "text": "You're welcome"
                    }
                ]
            }
        ]
    },

    #bell path
    {
        "type": "conditional",
        "if": {
            "has_hound_bell": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The object grows warm in Carmen's hands, almost burning."
                    },
                    {
                        "speaker": "Narration",
                        "text": "A bell rings."
                    },
                    {
                        "speaker": "Rio",
                        "text": "What was that?"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "That sound-"
                    },
                    {
                        "speaker": "Narration",
                        "text": "The object twists and reshapes into a strange bell. The tiny hound has now become the handle, it's tail the clapper, and the bell itself was engraved with the eyes of the hound."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "That bell... it looks like it can summon the hound."
                    },
                    {
                        "speaker": "Rio",
                        "text": "That feels unsafe. It's safe, right?"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "That depends on Carmen."
                    },
                    {
                        "speaker": "Carmen",
                        "text": "..."
                    }
                ]
            }
        ]
    },

    #  move to temple wing
    {
        "type": "transition",
        "target_scene": "fighter_sight_hub"
    }
]