import threading

winCases = {
    (0, 2),
    (1, 0),
    (2, 1),
}

def checkwin(my_choice, friend_choice):
    """
    Check if the choices made by the player and their friend result in a win, loss, or tie in a game.

    Args:
        my_choice (int): An integer representing the player's choice.
        friend_choice (int): An integer representing the friend's choice.

    Returns:
        int: 0 if the choices result in a tie, 1 if the player wins, -1 if the player loses.
    """
    if my_choice == friend_choice:
        return 0
    elif (friend_choice, my_choice) in winCases:
        return 1
    else:
        return -1

class Player:
    id = 1

    def __init__(self, username, conn) -> None:
        self.id = Player.id
        Player.id += 1
        self.username = username
        self.conn = conn

    def sendMsg(self, msg: str) -> bool:
        self.conn.send(str(msg).encode())
        return True

    def recvMsg(self):
        msg = self.conn.recv(1024).decode()
        return msg



# new class
class Game:
    id = 1
    def __init__(self, player1, player2) -> None:
        self.id = Game.id
        Game.id += 1
        self.players = [player1, player2]
        self.friend_choice = None


    def broadcast(self, msg):
        for player in self.players:
            player.sendMsg(msg)

    def remove_player(self, player):
        index=self.players.index(player)
        self.players.remove(player)
        return index
    
    def endGame(self):
        self.broadcast("Game ended")
        for player in self.players:
            player.conn.close()

        print(f"Game with id {self.id} ended")


# handleClient
def handle_client(g,player,lock):
    choice = int(player.recvMsg())
    win_status = 0
    lock.acquire() # lock the game object score
    if g.friend_choice is not None: 
        lock.release() # lock the game object score
        win_status = checkwin(choice, g.friend_choice)
        if win_status == 0:
            g.broadcast("The game is draw")
            return

        elif win_status == 1:
            username=player.username
            player.sendMsg("You won")
            g.remove_player(player)
            g.players[0].sendMsg("You lost")
            print(username, "won")
            return

        elif win_status == -1:
            username=player.username
            player.sendMsg("You lost")
            g.remove_player(player)
            g.players[0].sendMsg("You won")
            print(username, "lost")
            return
    
        g.endGame()

    else:
        g.friend_choice = choice
        lock.release()

def handle_game(g):
    lock=threading.Lock()
    t1=threading.Thread(target=handle_client,args=(g,g.players[0],lock))
    t2=threading.Thread(target=handle_client,args=(g,g.players[1],lock))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Game ended")