forest_bell_scene = [

    # Continue through the Forest
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The forest path narrows as the group continues deeper between the trees, until it disappears completely.", 
                "emotion": "neutral"
            },
            {
                "speaker": "Narration",
                "text": "Roots twist through the dirt between Carmen's boots, forcing each step to stay measured.",
                "emotion": "neutral"
            },
            {
                "speaker": "Rio",
                "text": "If this temple really exists, someone seriously picked the worst possible place to put it. Aren't temples usually reachable?",
                "emotion": "casual"
            },
            {
                "speaker": "Yohan",
                "text": "It entirely depends on the practice of the temple. Isolation of religious structures isn't uncommon, it usually represents some kind of significance.",
                "emotion": "analytical"
            },
            {
                "speaker": "Carmen",
                "text": "I don't think that's what Rio means... Or at least what I think.",
                "emotion": "cautious"
            },
            {
                "speaker": "Yohan",
                "text": "Huh?",
                "emotion": "curious"
            },
            {
                "speaker": "Rio",
                "text": "What's on your mind?",
                "emotion": "curious"
            },
            {
                "speaker": "Carmen",
                "text": "Well... in both cases, the temple has an obvious presence. As well as an obvious figure of worship.",
                "emotion": "honest"
            },
            {
                "speaker": "Rio",
                "text": "Yeah so?",
                "emotion": "curious"
            },
            {
                "speaker": "Carmen",
                "text": "But there's been absolutely no sign that this temple even exists. And the noblewoman never mentioned a deity for the temple. Not even a name.",
                "emotion": "concern"
            },
            {
                "speaker": "Narration",
                "text": "A realization dawns on everyone. Carmen was right. All they've seen is forest around them, even after exploring every inch of the place.",
                "emotion": "neutral"
            },
            {
                "speaker": "Narration",
                "text": "Yohan shifts uncomfortably.",
                "emotion": "netural"
            },
            {
                "speaker": "Yohan",
                "text": "That doesn't make sense though. This place is bathed in magic.",
                "emotion": "adamant"
            },
            {
                "speaker": "Rio",
                "text": "Yeah, but magic forests aren't uncommon.",
                "emotion": "concern"
            },
            {
                "speaker": "Yohan",
                "text": "Not with this much magic though! Besides I'm sure the noblewoman gave us a deity name, you two just forgot it.",
                "emotion": "adamant"
            },
            {
                "speaker": "Carmen",
                "text": "Do you remember then?",
                "emotion": "serious"
            },
            {
                "speaker": "Narration",
                "text": "An uncomfortable silence falls on the three. It's like the forest is waiting for an answer.",
                "emotion": "neutral"
            },
            {
                "speaker": "Yohan",
                "text": "...There's too much magic to ignore it.",
                "emotion": "quiet"
            },
            {
                "speaker": "Rio",
                "text": "So I guess the temple is just hiding from us then.",
                "emotion": "sarcastic"
            }
        ]
    },

    # The Bell
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Whatever the case was, the three of them continued to search for any signs of a Temple besides just magic.",
                "emotion": "neutral"
            },
            {
                "speaker": "Narration",
                "text": "But Carmen freezes in place.",
                "emotion": "sudden"
            },
            {
                "speaker": "Narration",
                "text": "The sound is faint and maybe Carmen didn't even hear it at all. But the sound is unmistakable.",
                "emotion": "serious"
            },
            {
                "speaker": "Narration", 
                "text": "It was a bell.",
                "emotion": "shocked"
            },
            {
                "speaker": "Narration",
                "text": "Their fingers tighten around their own bell. It couldn't have been theirs. There was no clapper, and Carmen hadn't touched it at all. But Carmen couldn't be sure.",
                "emotion": "tense"
            },
            {
                "speaker": "Narration", 
                "text": "All of a sudden, the forest around them felt like it didn't exist at all.",
                "emotion": "distant"
            },
        ]
    },

    # Carmen falls behind
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Rio and Yohan continue ahead before noticing Carmen had disappeared from their side.",
                "emotion": "netural"
            },
            {
                "speaker": "Rio",
                "text": "Carmen?",
                "emotion": "confused"
            },
            {
                "speaker": "Narration",
                "text": "Rio turns back down the path to where Carmen had stopped. Carmen was facing away from them. Yohan scans the area around them carefully.",
                "emotion": "neutral"
            },
            {
                "speaker": "Yohan",
                "text": "Did you find something?",
                "emotion": "concerned?"
            }

        ]
    },

    # Bell Choice
    {
        "type": "choice",
        "options":[

            # Tell the truth
            {
                "text": "I heard a bell...",
                "result": {
                    "set": {
                        "bell_response": "truth"
                    }
                }
            },

            # Lie to the others
            {
                "text": "I...thought I heard something behind us.",
                "result": {
                    "set": {
                        "bell response": "lie"
                    }
                }
            },

            # Stay silent
            {
                "text": "It... it's nothing. Don't worry about it. I'll catch up.",
                "result": {
                    "set": {
                        "bell response": "silent"
                    }
                }
            }
        ]
    },

    
]