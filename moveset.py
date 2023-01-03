'''
NAME:           moveset.py
AUTHOR:         @jharrisong830
VERSION:        0.4
DATE:           01/03/23
DESCRIPTION:    Definition of moves and the Move class.
'''

from colorama import Fore

class Move:
    def __init__(self, name: str, mnemonic: str, description: str, dmg_low: int, dmg_high: int, mp_used: int=0, df_add: int=0):
        self.name=name
        self.mnemonic=mnemonic
        self.description=description
        self.dmg_low=dmg_low
        self.dmg_high=dmg_high
        self.mp_used=mp_used
        self.df_add=df_add
    
    def __str__(self, help=False):
        result=self.name+" ('"+self.mnemonic+"')"
        if help: result+=" - "+self.description
        if self.dmg_low!=0 or self.dmg_high!=0:
            result+=Fore.RED+"\n\tDMG: "+str(self.dmg_low)+" - "+str(self.dmg_high)+Fore.RESET
        if self.mp_used!=0: result+=Fore.LIGHTCYAN_EX+"\n\tMP COST: "+str(self.mp_used)+Fore.RESET
        if self.df_add!=0: result+=Fore.BLUE+"\n\tDF+: "+str(self.df_add)+Fore.RESET
        result+="\n"
        return result

sword_move=Move("Sword Slash", "swr", "A simple swing of a sword.", 2, 3)
fire_move=Move("Fire Spell", "fire", "A magical spell that sets an enemy ablaze.", 5, 7, 5)
nothing_move=Move("Do Nothing", "no", "Do absolutely nothing this turn.", 0, 0)
shield_move=Move("Shield", "shd", "Put up your shield to defend for one turn.", 0, 0, df_add=5)

DEFAULT_MOVES={"swr": sword_move, "fire": fire_move, "no": nothing_move, "shd": shield_move}