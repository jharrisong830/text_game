'''
AUTHOR:         @jharrisong830
VERSION:        0.2
DATE:           12/29/22
DESCRIPTION:    Main file for text-based game.
'''

import player

def player_turn(player: player.Player, opponent: player.Player):
    print("\n"+player.name+"'s Turn:\n")
    print(player)
    print("CHOOSE A MOVE (type move name in the command-prompt):")
    for action in player.moves:
        print(player.moves[action])
    while True:
        choice=input()
        if choice in player.moves: break
        print("Error: "+choice+" is not a valid move. Please try again.")
    player.deal_move(player.moves[choice], opponent)

def opponent_turn(player: player.Player, opponent: player.Player, move: str):
    print(opponent.name+"'s Turn:")
    opponent.deal_move(opponent.moves[move], player)

def battle(player: player.Player, opponent: player.Player):
    while True:
        player_turn(player, opponent)
        if opponent.is_dead():
            print("YOU WON!")
            break
        opponent_turn(player, opponent, "swr")
        if player.is_dead():
            print("YOU lost :(")
            break


        

if __name__=="__main__":
    print("Welcome to TEXT-BASED GAME (v 0.1)")
    print("This is a very early stage of a project I'm working on.")
    print("This version only contains a simple battle sequence. Formatting and display specs are subject to change.")
    while True:
        option=input("Type 's' to START GAME, or 'exit' to exit now: ")
        if option=="s" or option=="exit":
            break
    if option=="s":
        p1=player.Player(10, 5)
        enemy=player.Player(2, 0, name="Brute")
        battle(p1, enemy)
    print("Thank you for trying TEXT-BASED GAME (v 0.2)! Check back soon for more updates and features!")
    print("-john")