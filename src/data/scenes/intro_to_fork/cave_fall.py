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
                "emotion": "neutral"
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
               "emotion": "neutral"
           },
           {
               "speaker" :"Narration",
               "text": "Yohan carefully slides down the slope after them with considerably less grace than his dignity would like. Carmen goes over to offer Yohan a hand, but he refuses. Rio stifles a laugh.",
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
               "emotion": "teasing"
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
   {
       "type": "conditional",
       "if": {
           "cave_argument": "carmen"
       },
       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "...Fair point.",
                       "emotion": "accepting"
                   },
                   {
                       "speaker": "Yohan",
                       "text": "That would be reasonable, yes.",
                       "emotion": "agreeing"
                   }
               ]
           }
       ]
   },

   # Discussing the Hole
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "The hole definitely wasn't there before, right?",
               "emotion": "serious"
           },
           {
               "speaker": "Carmen",
               "text": "I didn't see it when I turned around. I was distracted, by the creature so, but still.",
               "emotion": "uneasy"
           },
           {
               "speaker": "Yohan",
               "text": "Because it wasn't naturally formed.",
               "emotion": "serious"
           },
           {
               "speaker": "Narration",
               "text": "Yohan walks toward the cave wall, brushing his fingres against the stone surface carefully.",
               "emotion": "neutral"
           },
           {
               "speaker": "Yohan", 
               "text": "This opening was intentionally created.",
               "emotion": "anaytical"
           },
           {
               "speaker": "Yohan",
               "text": "After you fell in Carmen, the hole began to close up. I don't think you noticed Rio.",
               "emotion": "serious"
           },
           {
               "speaker": "Yohan", 
               "text": "I barely managed to follow before the passage sealed itself.",
               "emotion": "excited"
           },
           {
               "speaker": "Rio",
               "text": "So the cave wanted us down here?",
               "emotion": "excited"
           },
           {
               "speaker": "Yohan",
               "text": "I deeply dislike the way you said it, but it's... something like that.",
               "emotion": "disturbed"
           }
       ]
   },

   # The Cave
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Narration",
               "text": "The cave feels wrong in ways Carmen struggles to describe.",
               "emotion": "uneasy"
           },
           {
               "speaker": "Narration",
               "text": "The walls resemble natural stone, but not consistently.",
               "emotion": "unsettling"
           },
           {
               "speaker": "Narration",
               "text": "Stone sections curve too smoothly. Others look deliberately uneven, as though something attempted to imitate natural formation from memory alone.",
               "emotion": "disturbing"
           },
           {
               "speaker": "Narration",
               "text": "The cave does not feel constructured.",
               "emotion": "serious"
           },
           {
               "speaker": "Narration",
               "text": "But it does not feel natural either.",
               "emotion": "serious"
           }
       ]
   },

   # Decision to move forward
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "Well. Staying here won't help us much.",
               "emotion": "serious"
           },
           {
               "speaker": "Yohan",
               "text": "With the original entrance completely sealed, the only way is forward.",
               "emotion": "analytical"
           },
           {
               "speaker": "Carmen",
               "text": "Then we move carefully.",
               "emotion": "determined"
           },
           {
               "speaker": "Narration",
               "text": "The three turn toward the singular tunnel stretching deeper ahead.",
               "emotion": "neutral"
           },
           {
               "speaker": "Narration",
               "text": "It resembles a natural cave passage at first glance.",
               "emotion": "uneasy"
           },
           {
               "speaker": "Narration",
               "text": "But the longer Carmen stares at it, the more it feels staged. As though something tried to recreate the laws of nature without full understanding them. Or had its own standards for how reality should behave.",
               "emotion": "disturbing"
           }
       ]
   },

   # Transition to next Scene
   {
       "type": "transition",
       "target_scene": "deep_tunnel"
   }

]