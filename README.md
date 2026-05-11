# Visual Novel Prototype

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/axkprogram/axk230162-angm-2305.001-Final-Project-SP2026.git>

## Description

Hello. 
This project is a Visual Novel Prototype(VN-P from this point on). Think of it like an alpha of a game. This is in the most basic sense the minimum playable slice of a game.
I had some mechanics in this code I wanted to implement according to my proposal:
        - An rpg mechanic (implemented)
        - A multi path story tree with character interaction (implemented)
        - a ui that was clear (implemented)
        - dice mechanic that got a random choice at certain point(this was removed due to crashing)

HOW TO PLAY:
- Run py project.py.
- Press the spacebar or left click on your mouse to progress through dialogue. 
- If you want to exit the game at anytime press ESC.
- To make a choice press 1, 2 , 3, or 4 to pick the choice you want.

THE STORY TREE:
- This was the first step of the process because without the story tree, this project goes downhill quickly
- I decided to have one continuous path that would later split into three major different paths.
- There are several settings: a forest, the first cave tunnel, the chamber with three different paths, the fighter path, the mage path, the dark path. The ends of each of the paths have different endings. 
- There are not only major choices that change the paths. There are choices that lead to character interaction. Not too many but enough to be diverese.
- To implement the story tree, I used several dictionaries. They're located in the data folder within src. (src/data/scenes). The scenes have the four paths in folders (src/data/scenes/intro_to_fork), (src/data/scenes/fighter), (src/data/scenes/mage), (src/data/scenes/dark). To keep the transitions organized there is a registry.py that makes names to be called upon. There's a scene manager to translate all of this. If and elif statements made for taking things like "speaker", "choice", "conditional", and managing how they are called upon.
- In the project there is VN story tree.md which has the basic framework description of the story tree. Mood, characters, character personalities, endings, choice outcomes, etc. This was copy pasted from a google doc, but this is here as proof that this is my project and it was not copied by anyone. For the story I took inspiration from the King in Yellow and some ideas I've had for a dnd campaign. This is where the following RPG battle comes into play.
- The game_loop.py runs the code has main screen rendering and pygame import for the Key downs. The controller takes care of ui and 

RPG BATTLE:
- There is a single enemy vs player rpg battle in each path, fighter path has one against a hound, mage path has one against a specter, and dark path has a strange monster.
- fighter and mage path have your traditional turn based rpg battles
- dark path is an "impossible battle", but this is scripted to win no matter what
- Since the text based adventures were banned I was under the impression it was because the scope was too small, and since a visual novel was just a text based adventure with pictures, I decided I wanted there to be a simple rpg mechanic in the game. There would only be one battle on each path.
- fighter path and mage path: the players three attacks and their own unique enemies with their own three attacks
        - hound has an attack that causes the player to skip a turn, the player has an attack to increase damage, but will be forced to skip a turn.
        - specter has an attack that attacks and stuns player, the player has an attack that does the same.
        - player will always attack first
- the dark path is unique because its a scripted fight.

UI: 
- This was mentioned before but the UI is clear with no overlapping text.
- Choices are readable and labeled.

DICE MECHANIC SCRAPPED:
- This was scrapped because it would not progress any further than just the choice.
- If I have the chance I'll implement it another day.

WHAT CAN BE IMPROVED:
- A prototype that leaves room for improvement.
- I didn't have time to make character portraits,  for this so these need to be improved on
- Ui right now is clear, but the Ui can also definitely improved.
- Battle UI needs to be improved
- The dark path's scripted rpg battle is not working how I would like, but it is functional and doesn't hurt the story.

THE SRC:
- controller.py and game_loop.py make up the engine of the game.
- scene_manager.py translates the dictionary.
- battle.py holds the data for the rpg character states.
- battle_manager.py translates the battle as well similar to the scene manager

REFLECTION:
- As interesting as it was of a process, and the fact I'm very interested in my own story and where its going to go, this was an exhausting project.
- I can't call this fun as much as it was stressful trying to work through bugs and finding the typos the scene scripts when it comes to things like "choice" and "type" and "options". 
- This was an interesting project and maybe I'll try again another day, with help.