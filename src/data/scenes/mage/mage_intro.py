mage_intro_scene = [

     {
        "type": "background",
        "image": "cave_tunnel.jpg"
    },
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Yohan",
                "text": "Look at these engravings."
            },
            {
                "speaker": "Yohan",
                "text": "The language stops abruptly...unfinished. Then they start over."
            },
            {
                "speaker": "Yohan",
                "text": "Like authors carving over each other?"
            },
            {
                "speaker": "Rio",
                "text": "Didn't the noblewoman hire us to find a temple?"
            },
            {
                "speaker": "Rio",
                "text": "Not get distracted by every wall we see?"
            },
            {
                "speaker": "Carmen",
                "text": "What if the cave is the temple?"
            },
            {
                "speaker": "Rio",
                "text": "...I hadn't considered that."
            },
            {
                "speaker": "Yohan",
                "text": "If that's true..."
            },
            {
                "speaker": "Yohan",
                "text": "We may be uncovering history no one has seen in centuries."
            }
        ]
    },

    # Carmen internal
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen isn't convinced this is the temple itself."
            },
            {
                "speaker": "Narration",
                "text": "But whatever they're searching for feels closer now."
            },
        ]
    },

    #enemy appears
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Yohan suddenly raises an arm, stopping the others."
            },
            {
                "speaker": "Yohan",
                "text": "Wait. Something's here."
            },
            {
                "speaker": "Narration",
                "text": "A shrill screech echoes through the tunnel."
            },
            {
                "speaker": "Narration",
                "text": "A specter descends from above, its form flickering between smoke and bone."
            },
            {
                "speaker": "Rio",
                "text": "I don't think I can punch something that's already dead."
            },
            {
                "speaker" : "Rio",
                "text": "Got any ideas, Mr. Tower Mage?"
            },
            {
                "speaker": "Yohan",
                "text": "Yes. I'll handle it myself."
            }
        ]
    },

    # battle
    {
        "type": "battle",
        "player": "YOHAN",
        "enemy": "SPECTER"
    },

    # after battle
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The specter lets out one final distorted cry."
            },
            {
                "speaker": "Narration",
                "text": "Its form unravels into mist and vanishes."
            },
            {
                "speaker": "Narration",
                "text": "Something remains where it fell."
            },
            {
                "speaker": "Narration",
                "text": "A small statue with tightly curled ram horns, bird wings on its back and hands pressed together in prayer."
            },
            {
                "speaker": "Rio",
                "text": "Why did it leave a creepy souvenir?"
            }
        ]
    },

    # artifact choice
    {
        "type": "choice",
        "options": [

            {
                "text": "Have Yohan analyze the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_talisman_of_spirit": True
                    }
                }
            },
            {
                "text": "Have Rio destroy the object.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_spirit_gem": True
                    }
                }
            },
            {
                "text": "Have Carmen keep the object",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "has_spirit_bell": True
                    }
                }
            }
        ]
    },

    # Talisman path
    {
        "type": "conditional",
        "if": {
            "has_talisman_of_spirit": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Yohan",
                        "text": "It's a Talismman of Spirit."
                    },
                    {
                        "speaker": "Yohan",
                        "text":  "An old ceremonial idol for spiritual rituals. The Mage Tower probably has more information."
                    },
                    {
                        "speaker": "Rio",
                        "text": "So we're carrying cursed decorations now."
                    },
                    {
                        "speaker": "Carmen",
                        "text": "It feels...calm."
                    }
                ]
            }
        ]
    },

    # gemstone path
    {
        "type": "conditional",
        "if": {
            "has_spirit_gem": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Rio crushes the statue against the floor."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Inside rests a glowing blue gemstone shaped like the specter's core"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Does destruction really need to be your first instinct?"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "At least now we know what was inside."
                    }
                ]
            }
        ]
    },

    # bell path
    {
        "type": "conditional",
        "if": {
            "has_spirit_bell": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The statue turns ice-cold in Carmen's hands."
                    },
                    {
                        "speaker": "Narration",
                        "text": "A bell rings"
                    },
                    {
                        "speaker": "Rio",
                        "text": "What was that?"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It was too small to be a temple bell."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Carmen freezes. That sound came from the broken bell already in their possession."
                    },
                    {
                        "speaker": "Narration",
                        "text": "The staute twists and reshapes."
                    },
                    {
                        "speaker": "Narration",
                        "text": "It becomes a bell: the handle carved into the statues original figure, flames engraved around its body, and a simple clapper hanging beneath."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It looks like that bell can summon the specter we just fought."
                    },
                    {
                        "speaker": "Rio",
                        "text": "That sounds dangerous."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "That depends entirely on how Carmen uses it."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Carmen says nothing, but the weight of the bell feels heavier than before."
                    }
                ]
            }
        ]
    },

    #move to the mage_spirit_hub
    {
        "type": "transition",
        "target_scene": "mage_spirit_hub"
    }
]