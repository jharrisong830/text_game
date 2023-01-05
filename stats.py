'''
NAME:           stats.py
AUTHOR:         @jharrisong830
VERSION:        n/a
DATE:           01/03/23
DESCRIPTION:    wip implementing stats
'''

from colorama import Fore
from attributes import Attribute
class Stat:
    def __init__(self, turns: int):
        self.turns=turns
    
    def use(self):
        self.turns-=1

class RegenHP(Stat):
    def __init__(self, turns: int, hp: int):
        super().__init__(turns)
        self.hp=hp

class RegenMP(Stat):
    def __init__(self, turns: int, mp: int):
        super().__init__(turns)
        self.mp=mp

class Defense(Stat):
    def __init__(self, turns: int, df: int):
        super().__init__(turns)
        self.df=df

# class Stat:
#     def __init__(self, name: str, description: str, attribute: Attribute, stat_type: StatType, turns: int=1):
#         self.name=name
#         self.description=description
#         self.attribute=attribute
#         self.turns=turns
    
#     def __str__(self, help=False):
#         result=self.name
#         if help: result+=" - "+self.description
#         if self.mp_used!=0: result+=Fore.LIGHTCYAN_EX+"\n\tMP COST: "+str(self.mp_used)+Fore.RESET
#         if self.df_add!=0: result+=Fore.BLUE+"\n\tDF+: "+str(self.df_add)+Fore.RESET
#         result+="\n"
#         return result

# regen_hp=Stat("Regeneration", "Adds HP on every turn.", )
# STAT_LIBRARY={"regen_hp":}