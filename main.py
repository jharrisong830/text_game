'''
AUTHOR:         @jharrisong830
VERSION:        0.3
DATE:           12/29/22
DESCRIPTION:    Main file for text-based game.
'''

import player
import os
import time

def animated_print(str_out):
    for char in str_out:
        print(char, end="", flush=True)
        time.sleep(0.00000000001)

def player_turn(player: player.Player, opponent: player.Player):
    while True:
        animated_print(player.name+"'s Turn\n\n")
        animated_print(str(player)+"\n")
        animated_print("CHOOSE A MOVE (type move name in the command-prompt):\n\n")
        for action in player.moves:
            animated_print(str(player.moves[action])+"\n")
        choice=input()
        os.system("cls")
        if choice in player.moves: break
        animated_print("Error: '"+choice+"' is not a valid move. Please try again.\n")
        animated_print("\nPress any key to continue...")
        input()
        os.system("cls")
    animated_print(player.deal_move(player.moves[choice], opponent))
    animated_print("\nPress any key to continue...")
    input()
    os.system("cls")

def opponent_turn(player: player.Player, opponent: player.Player, move: str):
    animated_print(opponent.name+"'s Turn:\n\n")
    animated_print(str(opponent)+"\n\n")
    animated_print(opponent.deal_move(opponent.moves[move], player))
    animated_print("\nPress any key to continue...")
    input()
    os.system("cls")

def battle(player: player.Player, opponent: player.Player):
    while True:
        player_turn(player, opponent)
        if opponent.is_dead():
            animated_print("YOU WON!\n")
            break
        opponent_turn(player, opponent, "swr")
        if player.is_dead():
            animated_print("YOU lost :(\n")
            break
    animated_print("\nPress any key to continue...")
    input()
    os.system("cls")

def process_story(story, ply: player.Player):
    for line in story:
        line=line.strip()
        if line.startswith("//"): continue
        elif line.startswith("..."):
            animated_print("Press any key to continue...")
            input()
            os.system("cls")
        elif line.startswith("ENEMY"):
            enemy_properties=line[6:].split()
            enemy=player.Player(enemy_properties[0], int(enemy_properties[1]), int(enemy_properties[2]))
            battle(ply, enemy)
        elif line.startswith("\\n"):
            animated_print("\n")
        else:
            animated_print(str(line).replace("<PLAYER_NAME>", ply.name))



        

if __name__=="__main__":
    animated_print("Welcome to TEXT-BASED GAME (v 0.3)\n")
    animated_print("This is a very early stage of a project I'm working on.\n")
    animated_print("This version only contains a simple battle sequence. Formatting and display specs are subject to change.\n")
    while True:
        animated_print("Type 's' to START GAME, or 'exit' to exit now: ")
        option=input()
        if option=="s" or option=="exit":
            os.system("cls")
            break
    if option=="s":
        story=open("story.txt", 'r')
        animated_print("Enter your character's name: ")
        name=input()
        os.system("cls")
        p1=player.Player(name, 10, 5)
        process_story(story, p1)