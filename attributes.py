'''
NAME:           attributes.py
AUTHOR:         @jharrisong830
VERSION:        n/a
DATE:           01/03/23
DESCRIPTION:    wip implementing attributes
'''

from colorama import Fore

class Attribute:
    def __init__(self, name: str, value: int=0, color: str=Fore.RESET):
        self.name=name
        self.value=value
        self.color=color
    
    def __str__(self):
        return self.color+self.name+": "+self.value+Fore.RESET+"\n"
    



hp=Attribute("HP", color=Fore.GREEN)
mp=Attribute("MP", color=Fore.LIGHTCYAN_EX)

BASE_ATTRIBUTES=set(hp, mp)