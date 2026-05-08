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
    {
        "type": "conditional",
        "if": {
            "fall_response": "reassure"
        },

        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "Good. I'm glad. Would've been awkward if my rescue failed.",
                        "emotion": "playful"
                    },
                    {
                        "speaker": "Narration",
                        "text": "Rio sounds almost disappointed that the situation wasn't more dangerous.",
                        "emotion": "neutral"
                    }
                ]
            }
        ]
    },

    # Complain response
   {
       "type": "conditional",
       "if": {
           "fall_response": "complain"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "That means you're alive enough to complain. That's a good.",
                       "emotion": "amused"
                   },
                   {
                       "speaker": "Narration",
                       "text": "Rio laughs while brushing dust from her shoulder.",
                       "emotion": "neutral"
                   }
               ]
           }
       ]
   },

   # Ask about Rio
   {
       "type": "conditional",
       "if": {
           "fall_response": "rio_check"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "Aw, worried about me?",
                       "emotion": "smug"
                   },
                   {
                       "speaker": "Rio",
                       "text": "Don't worry. I've survived worse than jumping into mystery holes.",
                       "emotion": "confident"
                   }
               ]
           }
       ]
   },

   # Yohan Arrives
]