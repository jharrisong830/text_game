'''
NAME:           stats.py
AUTHOR:         @jharrisong830
VERSION:        n/a
DATE:           01/03/23
DESCRIPTION:    wip implementing stats
'''

from colorama import Fore

class Stat:
    def __init__(self, name: str, description: str, attribute: str, turns: int=1):
        self.name=name
        self.description=description
        self.attribute=attribute
        self.turns=turns
    
    def __str__(self, help=False):
        result=self.name
        if help: result+=" - "+self.description
        if self.mp_used!=0: result+=Fore.LIGHTCYAN_EX+"\n\tMP COST: "+str(self.mp_used)+Fore.RESET
        if self.df_add!=0: result+=Fore.BLUE+"\n\tDF+: "+str(self.df_add)+Fore.RESET
        result+="\n"
        return result

regen_hp=Stat("Regeneration", "Adds HP on every turn.", "hp")
#STAT_LIBRARY={"regen_hp":}