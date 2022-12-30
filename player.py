'''
AUTHOR:         @jharrisong830
VERSION:        0.3
DATE:           12/29/22
DESCRIPTION:    Player class and methods.
'''

import moveset
import random

class Player:
    def __init__(self, name: str, max_hp: int, max_mp: int, max_df: int=0, df: int=0):
        self.name=name
        
        self.max_hp=max_hp
        self.hp=self.max_hp

        self.max_mp=max_mp
        self.mp=self.max_mp

        self.max_df=max_df
        self.df=df


        self.moves=moveset.DEFAULT_MOVES

        self.items={} #TODO implement items
    
    def __str__(self, with_name=True):
        result=""
        if with_name: result+=self.name+"\n"
        result+="HP: "+str(self.hp)+"\n"
        result+="MP: "+str(self.mp)+"\n"
        result+="DF: "+str(self.df)+"\n"
        return result
    
    def deal_move(self, move: moveset.Move, recipient):
        result=""
        if move.mnemonic=="no":
            result+=self.name+" did nothing!\n"
        else:
            result+=self.name+" used "+move.name+"\n"
            damage=int(round(random.uniform(move.dmg_low, move.dmg_high)))-recipient.df
            recipient.df=recipient.max_df
            if damage<0:
                damage=0
                result+=recipient.name+" lost 0 HP\n"
            if damage!=0:
                recipient.hp-=damage
                result+=recipient.name+" lost "+str(damage)+" HP\n"
            if move.mp_used!=0:
                self.mp-=move.mp_used
                result+=self.name+" used "+str(move.mp_used)+" MP\n"
            if move.df_add!=0:
                self.df+=move.df_add
                result+=self.name+" gained "+str(move.df_add)+" DF for this turn\n"
            result+="\n"+self.name+"'s Current Stats:\n"
            result+=self.__str__(with_name=False)
        return result
    
    def is_dead(self):
        return True if self.hp<=0 else False
    
    def add_move(self, move: moveset.Move):
        self.moves[move.name]=move