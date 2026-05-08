cave_fall_scene = [

    # Fall Stops
    {
        "type": "dialogue",
        "lines":[
            {
                "speaker": "Narration",
                "text": "Air tears past you. Everything collapsing into darkness.",
                "emotion": "tense"
            },
            {
                "speaker": "Rio",
                "text": "I've got you-!",
                "emotion": "strained"
            },
            {
                "speaker": "Narration",
                "text": "Rio's arms wrap around Carmen, before the two of them slam into the uneven ground together.",
                "emotion": "chaotic"
            },
            {
                "speaker": "Narration",
                "text": "Dust erupts around them, swallowing the cave floor in a thick haze.",
                "emotion": "netural"
            },
            {
                "speaker": "Narration", 
                "text": "Once the dust finally settles, Rio slowly releases Carmen, having shielded most of the impact with her own body.",
                "emotion": "neutral"
            }
        ]
    },

    # Rio checks on Carmen
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Rio",
                "text": "You alive down there, Carmen?",
                "emotion": "teasing concern"
            },
            {
                "speaker": "Narration",
                "text": "Rio grins despite the rough landing, clearly more energized by the situation than bothered by it.",
                "emotion": "neutral"
            }
        ]
    },

    # Carmen Response Choice
    {
        "type": "choice",
        "options": [
            
            # Reassure
            {
                "text": "I'm okay, thanks to you.",
                "result": {
                    "set": {
                        "fall_response": "reassure"
                    }
                }
            },

            # Complain
            {
                "text": "Yeah... That's going to bruise tomorrow.",
                "result": {
                    "set": {
                        "fall_response": "complain"
                    }
                }
            },

            # Ask about Rio
            {
                "text": "What about you? You took most of the impact.",
                "result": {
                    "set": {
                        "fall_response": "rio_check"
                    }
                }
            }
        ]
    },

    # Reassure response
]