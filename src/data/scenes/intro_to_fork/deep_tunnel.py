deep_tunnel_scene = [
       # Moving through the Tunnel
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The tunnel stretches forward in a slow descent beneath the earth.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Narration",
                "text": "Their footsteps echo strangely through the passage, delayed by half-seconds that feel slightly too long.",
                "emotion": "unnatural"
            }
        ]
    },

    # Rio Notices the walls
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "This place doesn't look natural anymore. It looks built.",
               "emotion": "serious"
           },
           {
               "speaker": "Yohan",
               "text": "It's more like it's been restructured.",
               "emotion": "corrective"
           },
           {
               "speaker": "Rio",
               "text": "That's basically the same thing.",
               "emotion": "skeptical"
           }
       ]
   },

   # Player Response
   {
       "type": "choice",
       "options": [
           
           # Side with Rio
           {
               "text": "I think Rio's right. This feels intentionally made.",
               "result" : {
                   "set": {
                       "tunnel_alignment": "rio"
                   }
               }
           },

           # Side with Yohan
           {
               "text": "Yohan's words make more sense, it doesn't feel built from scratch.",
               "result": {
                   "set": {
                       "tunnel_alignment": "yohan"
                   }
               }
           },

           # Neutral
           {
               "text": "You both basically arrived at the same conclusion.",
               "result": {
                   "set": {
                       "tunnel_alignment": "carmen"
                   }
               }
           }
       ]
   },

   # Rio Alignment
   {
       "type": "conditional",
       "if": {
           "tunnel_alignment":"rio"
       },
       
       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "See? Carmen gets what I'm saying.",
                       "emotion": "approving",
                   },
                   {
                       "speaker": "Yohan",
                       "text": "I didn't say she was wrong.",
                       "emotion": "dry"
                   },
               ]
           }
       ]
   },

   # Yohan Alignment
   {
      "type": "conditional",
      "if": {
          "tunnel_alignment": "yohan"
      },

      "true": [
          {
              "type": "dialogue",
              "lines": [
                  {
                      "speaker": "Yohan",
                      "text": "Exactly, there's a distinction.",
                      "emotion": "approving"
                  },
                  {
                      "speaker": "Rio",
                      "text": "Only to people who like to make things more complicated.",
                      "emotion": "challenging"
                  }
              ]
          }
      ] 
   },

   # Carmen alignment
   {
       "type": "conditional",
       "if": {
           "tunnel_alignment": "carmen"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Yohan",
                       "text": "Not entirely. Construction obeys intention from the beginning.",
                       "emotion": "serious"
                   },
                   {
                       "speaker": "Yohan",
                       "text" : "This place feels like something natural was altered.",
                       "emotion": "uneasy"
                   },
                   {
                       "speaker": "Rio",
                       "text": "Still sounds like building something to me.",
                       "emotion": "skeptical"
                   }
               ]
           }
       ]
   },

   # Yohan staying calm
   {
       "type": "dialogue",
       "lines":[
           {
               "speaker": "Rio",
               "text": "Honestly, it sounds like you're juust trying to stay calm.",
               "emotion": "observant"
           },
           {
               "speaker": "Narration",
               "text": "Yohan doesn't respond.",
               "emotion": "observant"
           },
           {
               "speaker": "Narration",
               "text": "Not disagreement, but not confirmation either.",
               "emotion": "neutral"
           }
       ]
   },

   # Someone was here
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "Either way, it means that someone was here before us, right?",
               "emotion": "serious"
           },
           {
               "speaker": "Narration",
               "text": "Yohan doesn't answer immediately.",
               "emotion": "tense"
           },
           {
               "speaker": "Narration",
               "text": "The silence feels like an answer Carmen doesn't want.",
               "emotion": "uneasy"
           }
       ]
   },

   # Carmen touches the wall
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Narration",
               "text": "Carmen runs their fingers carefully along the wall.",
               "emotion": "neutral"
           },
           {
               "speaker": "Narration",
               "text": "Faint engravings stretch across the stone surface.",
               "emotion": "serious"
           },
           {
               "speaker": "Narration",
               "text": "The markings stop and start abruptly, incomplete in strange places.",
               "emotion": "unsettling"
           },
           {
               "speaker": "Narration",
               "text": "Like something forgotten was trying desperately to remember itself.",
               "emotion": "disturbing"
           },
           {
               "speaker": "Narration",
               "text": "The wall hums softly beneath Carmen's fingertips. Acknowledging them.",
               "emotion": "unnatural"
           },
           {
               "speaker" : "Carmen",
               "text": "-!",
               "emotion": "startled"
           },
           {
               "speaker": "Narration",
               "text": "Carmen jerks their hand away immediately.",
               "emotion": "panic"
           },
           {
               "speaker": "Rio",
               "text": "You alright there Carmen?",
               "emotion": "concern"
           }
       ]
   },

   # Wall Response
   {
       "type": "choice",
       "options": [
           
           # Lie
           {
               "text": "Nothing. Just a spider.",
               "result": {
                   "set": {
                       "wall_response": "lie"
                   }
               }
           },

           # Truth
           {
               "text": "I thought I felt something from the wall.",
               "result": {
                   "set": {
                       "wall_response": "truth"
                   }
               }
           }
       ]
   },

   # Lie Response
   {
       "type": "conditional",
       "if": {
           "wall_response": "lie"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "A spider scared you that badly?",
                       "emotion": "teasing"
                   },
                   {
                       "speaker": "Yohan",
                       "text": "... Must've been a big spider.",
                       "emotion": "skeptical"
                   },
                   {
                       "speaker": "Narration",
                       "text": "Yohan studies the wall more carefully afterward.",
                       "emotion": "neutral"
                   }
               ]
           }
       ]
   },

   # Truth Response
   {
       "type": "conditional",
       "if": {
           "wall_response": "truth"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Rio",
                       "text": "...The wall?",
                       "emotion": "uneasy"
                   },
                   {
                       "speaker": "Carmen",
                       "text": "like it reacted when I touched it.",
                       "emotion": "concerned"
                   },
                   {
                       "speaker": "Narration",
                       "text": "Yohan's expression darkens slightly.",
                       "emotion": "uneasy"
                   }
               ]
           }
       ]
   },

   # Engravings
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Yohan",
               "text": "These engravings aren't random.",
               "emotion": "focused"
           },
           {
               "speaker": "Yohan",
               "text": "They're methodical. There's a purpose to each of them, even if they end abruptly.",
               "emotion": "serious"
           },
           {
               "speaker": "Rio",
               "text": "Soooooo, what does that mean for us?",
               "emotion": "direct"
           },
           {
               "speaker": "Yohan",
               "text": "It means someone- or something- was doing something here. Not just living here",
               "emotion": "serious"
           },
           {
               "speaker": "Carmen",
               "text": "That's not reassuring.",
               "emotion": "uneasy"
           }
       ]
   },

   # The Cave Responds
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Narration",
               "text": "The cave suddenly shifts around them.",
               "emotion": "shock"
           },
           {
               "speaker": "Narration",
               "text": "But not physically.",
               "emotion": "unnatural"
           },
           {
               "speaker": "Narration",
               "text": "It's like something in the cave rushes past the three of them at impossible speed. Making itself known.",
               "emotion": "disturbing"
           },
           {
               "speaker": "Narration",
               "text": "Although there was no one else but the three of them in the cave, Carmen feels something snickering. But they say nothing about it.",
               "emotion": "disturbing"
           }
       ]
   },

   # The Group Acknowledges it
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Rio",
               "text": "...Okay. Tell me I'm not the only one who felt that.",
               "emotion": "uneasy"
           },
           {
               "speaker": "Yohan",
               "text": "Unfortunately not.",
               "emotion": "serious"
           },
           {
               "speaker": "Carmen",
               "text": "I felt it too.",
               "emotion": "quietly"
           },
           {
               "speaker": "Rio",
               "text": "I really don't like when we both agree on something.",
               "emotion": "uneasy humor"
           },
           {
               "speaker": "Yohan",
               "text": "Consistency is comforting.",
               "emotion": "matter-of-fact"
           },
           {
               "speaker": "Rio",
               "text": "That's exactly what I don't like.",
               "emotion": "dry"
           }
       ]
   },

   # Carmen Prevents Argument
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Carmen",
               "text": "Let's just keep moving you two. Before you start arguing again.",
               "emotion": "tired amusement"
           },
           {
               "speaker": "Narration",
               "text": "Rio and Yohan glare at each other briefly.",
               "emotion": "neutral"
           },
           {
               "speaker": "Rio",
               "text": "...Fine",
               "emotion": "accepting"
           },
           {
               "speaker": "Yohan",
               "text": "Agreed.",
               "emotion": "accepting"
           },
           {
               "speaker": "Narration",
               "text": "Carmen exhales quietly in relief and steps forward.",
               "emotion": "neutral"
           }
       ]
   },

   # Second Bell
   {
       "type": "dialogue",
       "lines": [
           {
               "speaker": "Narration",
               "text": "The tunnel stretches forward in a way that makes distance feel uncertain.",
               "emotion": "uneasy"
           },
           {
               "speaker": "Narration",
               "text": "Steps echo too cleanly. Too evenly.",
               "emotion": "disturbing"
           },
           {
               "speaker": "Narration",
               "text": "Like something is replaying them.",
               "emotion": "unsettling"
           },
           {
               "speaker": "Narration",
               "text": "Then-",
               "emotion": "tense"
           },
           {
               "speaker": "Narration",
               "text": "A bell rings somewhere deeper within the cave.",
               "emotion": "shock"
           },
           {
               "speaker": "Narration",
               "text": "So perfectly out of place.",
               "emotion": "neutral"
           },
           {
               "speaker": "Narration",
               "text": "The sound cuts through the tunnel with impossible clarity for how faint it was.",
               "emotion": "unnatural"
           },
           {
               "speaker": "Narration",
               "text": "All three of them immediately freeze in place.",
               "emotion": "tense"
           }
       ]
   },

   # Transition
   {
       "type": "transition",
       "target_scene": "bell_anomaly"
   }
]