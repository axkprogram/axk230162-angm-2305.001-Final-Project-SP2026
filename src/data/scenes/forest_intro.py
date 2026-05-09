forest_intro_scene = [

    # Environment
    {
        "type": "dialogue",
        "lines":[
            {
                "speaker": "Narration",
                "text": "The forest stretches wide and dense, its canopy filtering daylight into long, controlled shafts.",
                "emotion": "neutral"
            },
            {
                "speaker": "Narration", 
                "text": "The path forward is not marked clearly, but it is navigable. Used often enough to be followed.",
                "emotion": "neutral"
            },
            {
                "speaker": "Narration",
                "text": "This is not an untouched wilderness. Just a place people pass through when necessary.",
                "emotion": "neutral"
            }
        ]
    },

    # Carmen Context
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "Carmen moves with steady focus, maintaining pace while keeping an eye out for anything that looks remotely like what they're looking for.",
                "emotion": "focused"
            },
            {
                "speaker": "Narration",
                "text": "At their side hangs a bell. It doesn't ring, but Carmen carries it anwyay. They don't carry it for the sound anyway.",
                "emotion": "neutral"
            },
            {
                "speaker": "Narration",
                "text": "It was given to them by an old friend. Donny, or Donovan. He had a matching bell.",
                "emotion": "reflective"
            },
            {
                "speaker": "Narration",
                "text": "He went on a solo adventure one day, promising to send letters to Carmen. But not a single letter ever arrived",
                "emotion": "serious"
            },
            {
                "speaker": "Narration",
                "text": "Donovan never told Carmen where he was going, leaving Carmen with absolutely nothing. Except for the bell.",
                "emotion": "serious"
            },
            {
                "speaker": "Narration",
                "text": "A bell that caught the attention of a passing noblewoman. Intrigued and convinced of... something, the noblewoman insisted that Carmen take this one request of hers.",
                "emotion": "serious"
            },
            {
                "speaker": "Narration",
                "text": "In exchange, the noblewoman promised to assist in Carmen's search for Donovan in anyway possible. It seemed an innocent enough request on the surface. Find a temple, and bring the noblewoman an artifact to prove the temple exists.",
                "emotion": "neutral"
            }
        ]
    },

    # Party intro
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "A sharp voice and strained laughter somewhere in further in front of them, remind Carmen that they weren't alone on this request.",
                "emotion": "realization"
            },
            {
                "speaker": "Rio",
                "text": "I'm sureeee that your magic monocles are working juuuuuust fine Mr. Tower Mage. I'm just saying that maybe we should rely on our own two eyes instead. You might've missed something.",
                "emotion": "passive aggressive"
            },
            {
                "speaker": "Narration",
                "text": "Rio was a trained fighter. A popular fighter in the captial city. There's a confidence and readiness in her posture that is unmatched. Rio also had a wickedly handsome smile. Even if she didn't have the friendliest of intentions",
                "emotion": "neutral"
            },
            {
                "speaker": "Yohan",
                "text": "You speak very confidently for someone who hasn't found anything either you know, Madame pretty fists. At least I'm trying to trace some kind of magic that resembles a holy temple. It's more usefully than playing with a sword.",
                "emotion": "retaliation"
            },
            {
                "speaker": "Narration",
                "text": "Yohan was a prodigy mage from the capital city's Mage Tower. Every action he takes is calculated and purposeful. While Yohan may not have the sweetest personality, he was incredibly pretty for a seemingly overworked mage.",
                "emotion": "neutral"
            },
            {
                "speaker": "Rio",
                "text": "You think way too much. I know it's in you mages' nature, but sometimes you just need to move forward.",
                "emotion": "direct"
            },
            {
                "speaker": "Yohan",
                "text": "And you don't think enough. Leaping with fists flying doesn't necessarily lead to success.",
                "emotion": "calm rebuttal"
            },
            {
                "speaker": "Narration",
                "text": "Carmen sighed somewhat amused by Yohan and Rio's disagreement. The two of them didn't necessarily get along, the two's methods often clashing with each other, causing petty arguments like this. But they both knew they had a common goal. That said...",
                "emotion": "netural"
            },
            {
                "speaker": "Narration",
                "text": "Yohan and Rio turn sharply towards Carmen, startling Carmen. The two have a look in their eyes that causes Carmen to take a hesitant step back and lift up their hands in mock surrender.",
                "emotion": "neutral"
            },
            {
                "speaker": "Carmen",
                "text": "W-what is it? Why are you looking at me like that?",
                "emotion": "nervous"
            },
            {
                "speaker": "Narration",
                "text": "Rio rests a hand on the hilt of her sword. Tilting her head, and flashing Carmen a charming smile, full of hidden intentions. Carmen grew more nervous."
            },
            {
                "speaker": "Rio",
                "text": "Who do you think is right?",
                "emotion": "curious"
            },
            {
                "speaker": "Narration",
                "text": "Yohan scoffs and folds his arms across his chest. Eyes pressed closed and brows furrowed. Carmen already knew where this was going.",
                "emotion": "neutral"
            },
            {
                "speaker": "Yohan",
                "text": "It's not a matter of who's right. It's obvious that it's better to take a safer approach.",
                "emotion": "frustrated"
            },
            {
                "speaker": "Narration",
                "text": "And because petty arguments like these became common, Carmen had become the designated peacekeeper. Against their will, but for the sake of the mission.",
                "emotion": "neutral"
            }
        ]
    },

    # Player Choice
    {
        "type": "choice", 
        "options": [
            {
                "text": "If we were in danger, standing around would only make things worse. It's better to keep moving even if you're stuck.",
                "result": {
                    "set": {
                        "party_alignment": "Rio"
                    }
                }
            },

            {
                "text": "Acting without thinking can lead to things that could've been avoided...It's better to think before you act.",
                "result": {
                    "set": {
                        "party_alignment": "Yohan"
                    }
                }
            },

            {
                "text": "Rushing in blind is reckless and leads to dangerous situations, but overthinking can also slow down our progress.",
                "result": {
                    "set": {
                        "party_alignment": "Carmen"
                    }
                }
            }
        ]
    },

    # Rio Response
    {
        "type": "conditional",
        "if": {
            "party_alignment": "Rio"
        },

        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "Rio flashes a brighter, genuine smile. It's almost blinding.",
                        "emotion": "neutral"
                    },
                    {
                        "speaker": "Rio",
                        "text": "Sound answer, Carmen. Logical enough for you Mr. Tower mage?",
                        "emotion": "approving"
                    },
                    {
                        "speaker": "Narration",
                        "text": "Yohan's face relaxes but his mouth is curled into a scowl. Or maybe a pout? Carmen couldn't really tell with his tone.",
                        "emotion":"neutral"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "It's the same as pushing a boulder up a mountain...but if you say so.",
                        "emotion": "disapproving"
                    }
                ]
            }
        ]
    },

    # Yohan Response
    {
       "type": "conditional",
       "if": {
           "party_alignment": "Yohan"
       },

       "true": [
           {
               "type": "dialogue",
               "lines": [
                   {
                       "speaker": "Narration",
                       "text": "Yohan puts a hand up to his mouth. Carmen knows he's hiding a smirk.",
                       "emotion": "neutral"
                   },
                   {
                       "speaker": "Yohan",
                       "text": "Exactly my point. Thanks for seeing reason, Carmen.",
                       "emotion": "approving"
                   },
                   {
                       "speaker": "Narration",
                       "text": "Rio's smile didn't fade, but it did fall flat on her face.",
                       "emotion": "neutral"
                   },
                   {
                       "speaker": "Rio",
                       "text": "You can't think your way through an enemy...but I guess you're right in a way.",
                       "emotion": "disapproving."
                   }
               ]
           }
       ]
    },
    
    # Carmen response
    {
        "type": "conditional",
        "if": {
            "party_alignment": "Carmen"
        },

        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Narration",
                        "text": "The two look thoughtful at Carmen's words. Rio bobbing her head side to side, agreable. Yohan slowly nods his head."
                    },
                    {
                        "speaker": "Rio",
                        "text": "...Fair enough. I'll trust you on this Carmen.",
                        "emotion": "accepting"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Your reasoning is hard to argue with. Very well.",
                        "emotion": "accepting"
                    }
                ]
            }
        ]
    },

    # Ending the Scene
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "No matter who's right and who's not, we're here by request remember? We should keep looking for that Temple.",
                "emotion": "determined"
            },
            {
                "speaker": "Rio",
                "text": "I feel like we've already circled the entire place though.",
                "emotion": "lost"
            },
            {
                "speaker": "Yohan",
                "text": "I'm inclined to agree with Rio, for once.",
                "emotion": "accepting"
            },
            {
                "speaker": "Narration",
                "text": "The group continues deeper into the forest, regardless.",
                "emotion": "neutral"
            }
        ]
    }
]