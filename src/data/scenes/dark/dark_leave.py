dark_leave_scene = [
       {
        "type": "background",
        "image": "temple.jpg"
    },

    # if object was placed but bell not rung
    {
        "type": "conditional",
        "if": {
            "dark_pedestal_complete": True
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The three stand at the staircase in silence."
                    },
                    {
                        "speaker": "Rio",
                        "text": "So that's it."
                    },
                    {
                        "speaker": "Rio",
                        "text": "We came all this way and leave empty-handed."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "At least we're leaving alive."
                    }
                ]
            },
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Carmen glances back toward the sealed chamber."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Something deep within calls Carmen back."
                    },
                    {
                        "speaker": "Narration",
                        "text": "A promise lingers. Carmen didn't want to know what it meant."
                    },
                    {
                        "speaker": "System",
                        "text": "Chapter End."
                    },
                    {
                        "speaker": "System",
                        "text": "Press Esc to quit"
                    }
                ]
            }
        ]
    },

    # if a player leaves with object
    {
        "type": "conditional",
        "if": {
            "dark_pedestal_complete": False
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                         "speaker": "Rio",
                        "text": "I vote we leave with our lives."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Agreed."
                    },
                    {
                        "speaker": "Rio",
                        "text": "We'll hand the noble this cursed statue and call it success."
                    }
                ]
            },
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "Still annoyed I couldn't smash it."
                    },
                    {
                        "speaker": "Yohan",
                        "text": "And I'm annoyed I couldn't understand it."
                    }
                ]
            },
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Carmen looks back one last time."
                    },
                    {
                        "speaker": "Narration",
                        "text": "The cave rumbles beneath their feet."
                    },
                    {
                        "speaker": "Narration",
                        "text": "Something calls Carmen back."
                    },
                    {
                        "speaker": "Narration",
                        "text": "A promise lingers. Carmen doesn't want to know what it means."
                    },
                    {
                        "speaker": "System",
                        "text": "Chapter End."
                    },
                    {
                        "speaker": "System",
                        "text": "Press ESC to quit."
                    }
                ]
            }  
        ]
    }
]