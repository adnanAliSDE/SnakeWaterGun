'''matching algorithm prototype for matching the players
input - player conn object and username
process- matches the user
output- create a game object and passes it to game handler
'''
import game

# make empty players list
players=[]
def match(player: player)-> int:
    if len(players)==0:
        players.append(player)
    else:
        g=Game(player,players[0])
        game.handleGame(g)
        print("matched")

    return 200