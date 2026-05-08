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
]