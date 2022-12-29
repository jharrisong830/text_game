'''
AUTHOR:         @jharrisong830
VERSION:        0.1
DATE:           12/29/22
DESCRIPTION:    Definition of moves and the Move class.
'''

class Move:
    def __init__(self, name: str, mnemonic: str, description: str, dmg: int, mp_used: int=0):
        self.name=name
        self.mnemonic=mnemonic
        self.description=description
        self.dmg=dmg
        self.mp_used=mp_used
    
    def __str__(self):
        result=self.name+" ("+self.mnemonic+") - "+self.description+"\n\tDMG: "+str(self.dmg)
        if self.mp_used!=0: result+="\n\tMP COST: "+str(self.mp_used)
        result+="\n"
        return result

sword_move=Move("Sword Slash", "swr", "A simple swing of a sword.", 2)
fire_move=Move("Fire Spell", "fire", "A magical spell that sets an enemy ablaze.", 5, 5)
nothing_move=Move("Do Nothing", "no", "Do absolutely nothing this turn.", 0)

DEFAULT_MOVES={"swr": sword_move, "fire": fire_move, "no": nothing_move}