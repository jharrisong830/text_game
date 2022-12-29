# text_game
An evolving project that aims to create a text-based adventure with a detailed battle system. Currently on v 0.2.
## Upcoming Features
- Defense attribute and moves related to defense
- Consumable items to use during battle
- More (unlockable) moves
- A simple demo story to be run in the main file
- ...even more soon!
## Changelog
### v 0.2 (12/29/22)
- Added variable damage (selects a random floating point number within an integer range, and rounding the result to the nearest integer)
- Added a simple defense move and capability of defense mechanics
    - Defense from the defense move is added only for one turn, and is reset to the player's default DF after an attack on the player is complete
    - If defense causes the damage done to be less than 0, then the damage is automatically set to 0
### v 0.1 (12/29/22)
- Game created!
- Very simple battle system with 3 moves (sword, fire, and nothing)
- Demo battle with a default character and easy-to-beat monster
- Basic implementations of the main file, Move class, and Player class