'''
AUTHOR:         @jharrisong830
VERSION:        0.2
DATE:           12/29/22
DESCRIPTION:    Player class and methods.
'''

import moveset
import random

class Player:
    def __init__(self, max_hp: int, max_mp: int, max_df: int=0, df: int=0, name: str="NEW_GAME"):
        self.max_hp=max_hp
        self.hp=self.max_hp

        self.max_mp=max_mp
        self.mp=self.max_mp

        self.max_df=max_df
        self.df=df

        self.name=name
        if self.name=="NEW_GAME": self.name=input("Enter your character's name: ")

        self.moves=moveset.DEFAULT_MOVES

        self.items={} #TODO implement items
    
    def __str__(self):
        result=self.name+"\n"
        result+="HP: "+str(self.hp)+"\n"
        result+="MP: "+str(self.mp)+"\n"
        result+="DF: "+str(self.df)+"\n"
        return result
    
    def deal_move(self, move: moveset.Move, recipient):
        if move.mnemonic=="no":
            print(self.name+" did nothing!")
        else:
            print(self.name+" used "+move.name)
            damage=int(round(random.uniform(move.dmg_low, move.dmg_high)))-recipient.df
            recipient.df=recipient.max_df
            if damage<0:
                damage=0
                print(recipient.name+" lost 0 HP")
            if damage!=0:
                recipient.hp-=damage
                print(recipient.name+" lost "+str(damage)+" HP")
            if move.mp_used!=0:
                self.mp-=move.mp_used
                print(self.name+" used "+str(move.mp_used)+" MP")
            if move.df_add!=0:
                self.df+=move.df_add
                print(self.name+" gained "+str(move.df_add)+" DF for this turn")
    
    def is_dead(self):
        return True if self.hp<=0 else False
    
    def add_move(self, move: moveset.Move):
        self.moves[move.name]=move