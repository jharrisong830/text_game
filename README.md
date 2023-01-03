# text_game
An evolving project that aims to create a text-based adventure with a detailed battle system. Currently on v 0.2.
## Upcoming Features
- More stats, attributes, and complexity in battles
- Clearer user interface
- Consumable items to use during battle
- More (unlockable) moves
- More expansive stories with multiple battles
- ...even more soon!
## Changelog
### v 0.4 (01/03/23)
- Colors for different attributes! (using the Python `colorama` module)
    - Red -> damage
    - Blue -> defense
    - Light cyan -> magic
    - Green -> health
- Added a "type 'h' for help" feature in the battle sequence
    - Descriptions of moves no longer displayed by default, only displayed in help mode
    - Reduces the time it takes to print all moves
    - Will experiment with other methods of reducing print time in future versions
- Minor formatting changes
### v 0.3 (12/29/22)
- Use of `os.system("cls")` to clear the command line after certain events (to prevent clutter)
- Added stalling functionality, where the program is stalled until the command line receives keyboard input
    - `Press any key to continue...` is displayed until a key is pressed
    - The command line is typically cleared after a stall
- Added an "animated" (`animated_print()`) print function, which prints out a string character-by-character without new lines (unless explicitly specified)
    - Almost all text in the game is printed in the animated style
- Added a demo story with a demo battle (see [`story.txt`](story.txt))
- Added a function that can read, process, and display a story from a text file, with `.startswith()` used to handle proper formatting and control flow
    - `...`: stalling the story, wait for keyboard input before continuting. After keyboard input is received, the command line will be cleared
    - `\n`: prints a new line (lines in the text file do not create new lines)
    - `ENEMY <name: str> <max_hp: int> <max_mp: int>`: indicates that a new enemy should be created with the specified attributes, and a battle with that enemy will be started
    - All other lines are printed to the command line
- Changes made to [`player.py`](player.py) and ['moveset.py](moveset.py) to enable compatability with `animated_print()`
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