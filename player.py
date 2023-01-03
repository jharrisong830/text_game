'''
NAME:           player.py
AUTHOR:         @jharrisong830
VERSION:        0.4
DATE:           01/03/23
DESCRIPTION:    Player class and methods.
'''

import moveset
import random
from colorama import Fore

class Player:
    def __init__(self, name: str, max_hp: int, max_mp: int, min_df: int=0):
        self.name=name
        
        self.max_hp=max_hp
        self.hp=self.max_hp

        self.max_mp=max_mp
        self.mp=self.max_mp

        self.min_df=min_df
        self.df=min_df


        self.moves=moveset.DEFAULT_MOVES

        self.items={} #TODO implement items
    
    def __str__(self, with_name=True):
        result=""
        if with_name: result+=self.name+"\n"
        result+=Fore.GREEN+"HP: "+str(self.hp)+Fore.RESET
        if self.hp<=5:
            result+=Fore.RED+" (DANGER)"+Fore.RESET
        result+="\n"
        result+=Fore.LIGHTCYAN_EX+"MP: "+str(self.mp)+Fore.RESET+"\n"
        result+=Fore.BLUE+"DF: "+str(self.df)+Fore.RESET+"\n"
        return result
    
    def deal_move(self, move: moveset.Move, recipient):
        result=""
        if move.mnemonic=="no":
            result+=self.name+" did nothing!\n"
        else:
            result+=self.name+" used "+move.name+"\n"
            damage=int(round(random.uniform(move.dmg_low, move.dmg_high)))-recipient.df
            recipient.df=recipient.min_df
            if damage<0:
                damage=0
                result+=recipient.name+" lost 0 HP\n"
            if damage!=0:
                recipient.hp-=damage
                result+=recipient.name+" lost "+Fore.RED+str(damage)+" HP"+Fore.RESET+"\n"
            if move.mp_used!=0:
                self.mp-=move.mp_used
                result+=self.name+" used "+Fore.LIGHTCYAN_EX+str(move.mp_used)+" MP"+Fore.RESET+"\n"
            if move.df_add!=0:
                self.df+=move.df_add
                result+=self.name+" gained "+Fore.BLUE+str(move.df_add)+" DF"+Fore.RESET+" for this turn\n"
            result+="\n"+self.name+"'s Current Stats:\n"
            result+=self.__str__(with_name=False)
        return result
    
    def is_dead(self):
        return True if self.hp<=0 else False
    
    def add_move(self, move: moveset.Move):
        self.moves[move.name]=move
