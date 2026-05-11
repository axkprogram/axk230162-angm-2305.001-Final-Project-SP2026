bell_anomaly_scene = [

     {
        "type": "background",
        "image": "cave_fall.jpg"
    },

    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The bell's sound lingers in Carmen's mind long after it stops.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "It was faint. Out of place. But so painfully familiar.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Narration",
                "text": "Something tightens violently in Carmen's chest.",
                "emotion": "panic"
            },
            {
                "speaker": "Narration",
                "text": "Something tightens violently in Carmen's chest.",
                "emotion": "panic"
            },
            {
                "speaker": "Narration",
                "text": "Before they realize it, their hands are clamped tightly over their ears.",
                "emotion": "panic"
            },
            {
                "speaker": "Narration",
                "text": "Their breathing becomes uneven.",
                "emotion": "panic"
            }
        ]
    },

    # Rio snaps Carmen out
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Rio",
                "text": "Carmen. Hey, hey look at me. look at me.",
                "emotion": "concern"
            },
            {
                "speaker": "Narration",
                "text": "Rio grabs Carmen's shoulders and gently shakes them.",
                "emotion": "urgent"
            },
            {
                "speaker": "Narration",
                "text": "Slowly, Carmen's breathing steadies.",
                "emotion": "relief"
            },
        ]
    },

    # Player choice
    {
        "type": "choice",
        "options": [
            # truth
            {
                "text": "I- I heard a bell.",
                "result": {
                    "set": {
                        "bell_response": "truth"
                    }
                }
            },

            # lie
            {
                "text": "It- it was nothing.",
                "result": {
                    "set": {
                        "bell_response": "lie"
                    }
                }
            }
        ]
    },

    # Truth branch
    {
        "type": "conditional",
        "if": {
            "bell_response": "truth"
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "A bell? Down here?",
                        "emotion": "confused"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "That's not possible.",
                        "emotion": "analytical"
                    },
                    {
                        "speaker": "Rio",
                        "text": "Yohan.",
                        "emotion": "scolding"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "I swear. I swear I heard it. Didn't you?",
                        "emotion": "desperate"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "You had to have heard it too.",
                        "emotion": "desperate"
                    },
                    {
                        "speaker": "Rio",
                        "text": "Hey, hey it's okay. We trust you. We know you wouldn't lie to us.",
                        "emotion": "gentle"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Which makes the fact neither me nor Rio heard this bell, significantly more concerning.",
                        "emotion": "serious"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "You heard something back in the forest as well.",
                        "emotion": "serious"
                    }
                ]
            }
        ]
    },

    # Lie Branch
    {
        "type": "conditional",
        "if": {
            "bell_response": "lie"
        },
        "true": [
            { 
                "type": "dialogue",
                "lines" :[
                    {
                        "speaker": "Rio",
                        "text": "It didn't look like nothing.",
                        "emotion": "concern"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "You don't need to hide it if something happened.",
                        "emotion": "serious"
                    },
                    {
                        "speaker": "Carmen",
                        "text": "Its nothing. It was nothing at all. I swear it was.",
                        "emotion": "desperate"
                    },
                    {
                        "speaker": "Narration",
                        "text": "Yohan and Rio both exchange a look and give each other a small nod.",
                        "emotion": "neutral"
                    },
                    {
                        "speaker": "Rio",
                        "text": "...Alright. But tell us if anything's wrong.",
                        "emotion": "concern"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Right now we're on this mission together, so we need to work together.",
                        "emotion": "concern"
                    }
                ]
            }
           
        ]
    },

    # Carmen apology
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "I... I'm sorry. I don't know why I reacted like that.",
                "emotion": "apologetic"
            },
            {
                "speaker": "Rio",
                "text": "Don't apologize for that.",
                "emotion": "gentle"
            },
            {
                "speaker": "Yohan",
                "text": "Just tell us if it happens again.",
                "emotion": "serious"
            }
        ]
    },

    # Carmen leads
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen forces their hands to unclench and steps forward to lead.",
                "emotion": "determined"
            },
            {
                "speaker": "Carmen",
                "text": "Let's keep moving.",
                "emotion": "determined"
            }
        ]
    },

    # Cave reacts
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The air feels heavier now.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "Closer.",
                "emotion": "unnatural"
            },
            {
                "speaker": "Narration",
                "text": "It clings to Carmen's skin, weighing on their chest like it wants to suffocate them.",
                "emotion": "panic"
            },
            {
                "speaker": "Narration",
                "text": "It feels like something in this cave was testing Carmen.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "Listening for their reaction.",
                "emotion": "horror"
            }
        ]
    },

    # Transition
    {
        "type": "transition",
        "target_scene" : "fork_in_tunnel"
    }
]