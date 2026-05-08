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
   }

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
                       "text" : "This place feel slike something natural was altered.",
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

   
]