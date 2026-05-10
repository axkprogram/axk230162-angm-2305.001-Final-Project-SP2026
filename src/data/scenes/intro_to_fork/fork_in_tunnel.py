fork_in_tunnel_scene = [
    
    #arrival at the fork
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The tunnel eventually opens into a wide stone chamber.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Narration",
                "text": "Three separate tunnels branch outward ahead of them.",
                "emotion": "serious"
            },
            {
                "speaker": "Narration",
                "text": "Of course, none of them feel naturally formed.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "They feel arranged.",
                "emotion": "unnatural"
            }
        ]
    },

    # Right path
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Rio",
                "text": "The right path looks promising.",
                "emotion": "focused"
            },
            {
                "speaker": "Rio",
                "text": "Gravel. Recently used. Occasional torches mounted on the walls. If someone's been here, maybe it leads out.",
                "emotion": "serious"
            },
            {
                "speaker": "Yohan",
                "text": "Or into a trap",
                "emotion": "skeptical"
            },
            {
                "speaker": "Yohan",
                "text": "The lighting is inconsistent. That makes it dangerous.",
                "emotion": "serious"
            }
        ]
    },

    #Left path
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Yohan",
                "text": "The left path is more structured.",
                "emotion": "focused"
            },
            {
                "speaker": "Yohan",
                "text": "Stonework. Even lighting. Predictable footing.",
                "emotion": "serious"
            },
            {
                "speaker": "Rio",
                "text": "It looks like a castle hallway built for ghosts.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Rio",
                "text": "It also looks like we're moving further into something instead of escaping",
                "emotion": "skeptical"
            }
        ]
    },

    #center path
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Carmen",
                "text": "What about the center path?",
                "emotion": "curious"
            },
            {
                "speaker": "Narration",
                "text": "The center path simply exists.",
                "emotion": "unnatural"
            },
            {
                "speaker": "Narration",
                "text": "It is narrow, dark, and overgrown with lush greenery. Unnatural because there is no dirt, just stone.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Narration",
                "text": "A faint light glows somewhere deeper inside.",
                "emotion": "mysterious"
            },
            {
                "speaker": "Narration",
                "text": "A few fireflies drift lazily near its entrance.",
                "emotion": "unnatural"
            },
            {
                "speaker": "Narration",
                "text": "Dust bends away from it.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "Even the light avoids touching it directly.",
                "emotion": "disturbing"
            },
            {
                "speaker": "Narration",
                "text": "Something inside...beckons to Carmen. Like its paying attention without revealing itself.",
                "emotion": "horror"
            }
        ]
    },

    #  Reaction to the center path
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Yohan",
                "text": "I'm surprised you're even asking.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Rio",
                "text": "Just look at it Carmen. You think we're going to get out that way?",
                "emotion": "teasing"
            },
            {
                "speaker": "Carmen",
                "text": "It feels like it already knows we're here.",
                "emotion": "uneasy"
            },
            {
                "speaker": "Yohan",
                "text": "All the more reason we should avoid it.",
                "emotion": "serious"
            },
            {
                "speaker": "Rio",
                "text": "For once I agree.",
                "emotion": "serious"
            }
        ]
    },

    # Path choice
    {
        "type": "choice",
        "options": [
            
            # Rio's path
            {
                "text": "Take the right path.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "route_state": "fighter"
                    }
                }
            },

            # Yohan's path
            {
                "text": "Take the left path.",
                "result": {
                    "action": "state_change",
                    "changes": {
                        "route_state": "mage"
                    }
                }
            },

            # Carmen path
            {
                "text": "Take the center path.",
                "result": {
                    "action": "state_change",
                     "changes": {
                        "route_state": "dark"
                    }
                }
            },
        ]
    },

    # Fighter Branch
    {
        "type": "conditional",
        "if": {
            "route_state": "fighter"
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "Good. It's a practical decision.",
                        "emotion": "approving"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Or reckless",
                        "emotion": "skeptical"
                    }
                ]
            }
        ]
    },

    # Mage Branch
    {
        "type": "conditional",
        "if": {
            "route_state": "mage"
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Yohan",
                        "text": "Logical decision.",
                        "emotion": "approving"
                    },
                    {
                        "speaker": "Rio",
                        "text": "A painfully boring one, too.",
                        "emotion": "dry"
                    }
                ]
            }
        ]
    },

    # Dark Branch
    {
        "type": "conditional",
        "if": {
            "route_state": "dark"
        },
        "true": [
            {
                "type": "dialogue",
                "lines": [
                    {
                        "speaker": "Rio",
                        "text": "...I hate this.",
                        "emotion": "uneasy"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Me too.",
                        "emotion": "uneasy"
                    },
                    {
                        "speaker": "Rio",
                        "text": "But we trust you.",
                        "emotion": "concern"
                    },
                    {
                        "speaker": "Yohan",
                        "text": "Tread carefully.",
                        "emotion": "serious"
                    }
                ]
            }
        ]
    },

    # transition based route
    {
        "type": "transition",
        "target_scene": "route_intro"
    }
]