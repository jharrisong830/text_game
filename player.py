'''
AUTHOR:         @jharrisong830
VERSION:        0.1
DATE:           12/29/22
DESCRIPTION:    Player class and methods.
'''

import moveset

class Player:
    def __init__(self, max_hp: int, max_mp: int, df: int=0, name: str="NEW_GAME"):
        self.max_hp=max_hp
        self.hp=self.max_hp

        self.max_mp=max_mp
        self.mp=self.max_mp

        self.df=df

        self.name=name
        if self.name=="NEW_GAME": self.name=input("Enter your character's name: ")

        self.moves=moveset.DEFAULT_MOVES

        self.items={}
    
    def __str__(self):
        result=self.name+"\n"
        result+="HP: "+str(self.hp)+"\n"
        result+="MP: "+str(self.mp)+"\n"
        return result
    
    def deal_move(self, move: moveset.Move, recipient):
        if move.mnemonic=="no":
            print(self.name+" did nothing!")
        else:
            print(self.name+" used "+move.name)
            recipient.hp-=move.dmg
            print(recipient.name+" lost "+str(move.dmg)+" HP")
            if move.mp_used!=0:
                self.mp-=move.mp_used
                print(self.name+" used "+str(move.mp_used)+" MP")
    
    def is_dead(self):
        return True if self.hp<=0 else False
    
    def add_move(self, move: moveset.Move):
        self.moves[move.name]=move