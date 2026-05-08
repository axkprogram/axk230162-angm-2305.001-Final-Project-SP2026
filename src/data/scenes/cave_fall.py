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
   {
       
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Narration",
               "text": "Loose stone shifts above Carmen and Rio.",
               "emotion": "netural"
           },
           {
               "speaker" :"Narration",
               "text": "Yohan carefully slides down the slope after them with considerably less grace than his dignity would like. Carmen goes over to offer Yohan a ahnd, but he refuses. Rio stifles a laugh.",
               "emotion": "neutral"
           },
           {
               "speaker": "Yohan",
               "text": "Neither of you saw a thing.",
               "emotion": "irritated"
           },
           {
               "speaker": "Narration",
               "text": "Yohan immediately adjusts his clothes and regains composure before assessing Carmen.",
               "emotion": "neutral"
           },
           {
               "speaker": "Yohan",
               "text": "You look alive at least. That's all that matters.",
               "emotion": "hidden relief"
           },
           {
               "speaker": "Rio",
               "text": "Not even a 'Carmen, thank goodness you're safe?'. What about me?",
               "emotions": "teasing"
           },
           {
               "speaker": "Yohan",
               "text": "You've been dramatic enough about their well being. And you've handled throws harder than that.",
               "emotion": "flat"
           }
       ]
   },

   # Argument starts
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "You really don't care for anyone other than yourself, do you?",
               "emotion": "challenging"
           },
           {
               "speaker": "Yohan",
               "text": "And you throw yourself into strange holes before thinking. We all have flaws",
               "emotion": "challenging"
           },
       ]
   },

   # Party Choice
   {
       "type": "choice",
       "options": [
           
           # Side with Rio
           {
               "text": "You could sound a bit more concerned Yohan...",
               "result": {
                   "set": {
                       "cave_argument": "rio"
                   }
               }
           },

           # Side with Yohan
           {
               "text": "While I'm thankful, jumping into the hole after me wasn't safe either.",
               "result": {
                   "set": {
                       "cave_argument": "yohan"
                   }
               }
           },

           # Neutral
           {
               "text": "Can we survive the strange cave first before arguing again?",
               "result":{
                   "set":{
                       "cave_argument": "carmen"
                   }
               }
           }
       ]
   },

   # Rio Side Response
   {
       "type": "conditional",
       "if":{
           "cave_argument": "rio"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                        "text": "A little concern never hurt anyone, right Carmen?",
                        "emotion": "smug"
                   },
                   {
                       "speaker": "Yohan",
                       "text": "Excessive concern wouldn't have changed anything.",
                       "emotion": "annoyed"
                   }
               ]
           }
       ]
   },

   # Yohan side response
   {
       "type": "conditional",
       "if": {
           "cave_argument": "yohan"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Yohan",
                       "text": "Exactly my point, thank you Carmen.",
                       "emotion": "approving"
                   },
                   {
                       "speaker": "Rio",
                       "text": "And yet my irrational actions saved Carmen.",
                       "emotion": "Challenging"
                   }
               ]
           }
       ]
   },

   # Carmen Side Response
]