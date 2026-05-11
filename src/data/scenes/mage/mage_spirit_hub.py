mage_spirit_hub_scene = [
       {
        "type": "background",
        "image": "temple.jpg"
    },
    # arrival
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The tunnel widens ahead.",
            },
            {
                "speaker": "Rio",
                "text": "I see an opening!"
            },
            {
                "speaker": "Narration",
                "text": "Rio rushes forward before anyone can stop her."
            },
            {
                "speaker": "Yohan",
                "text": "Rio-- Slow down!"
            },
            {
                "speaker":"Narration",
                "text": "Yohan hurries after her, while Carmen follows close behind"
            }
        ]
    },

    # chamber reveal
    {
        "type": "dialogue",
        "lines": [
            {
                "speaker": "Narration",
                "text": "The three emerge into a circular chamber carved entirely from stone."
            },
            {
                "speaker": "Narration",
                "text": "A pedestal stands in the center, its top cacrved into a shallow receptacle."
            },
            {
                "speaker": "Narration",
                "text": "Across from the tunnel is a sealed stone door."
            },
            {
                "speaker": "Narration",
                "text": "A specter surrounded by blue flames is engraved into its surface."
            },
            {
                "speaker": "Narration",
                "text": "A staircase nearby appears to lead back to the surface."
            },
            {
                "speaker": "Rio",
                "text": "So this is the end of the path..."
            },
            {
                "speaker": "Yohan",
                "text": "We should look carefully before deciding anything."
            }
        ]
    },

    # move to menu hub
    {
        "type": "transition",
        "target_scene": "mage_spirit_hub_menu"
    }
]