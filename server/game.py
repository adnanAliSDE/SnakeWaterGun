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
    def __init__(self,conn,addr,username):
	    self.conn=conn
        self.addr=addr
        self.username=username

    def sendMsg(self,msg):
        conn.send(str(msg).encode())

    def recvMsg(self):
        msg=self.conn.recv(1024).decode()
        return msg

class Game:
    def __init__(self,player1,player2):
        self.players=[player1,player2]
        self.friend_choice = None

    def broadcast(self,msg):
        for player in self.players:
            player.sendMsg(msg)
    
    def removePlayer(self,player):
        player_index=self.players.index(player)
        self.players.pop(player_index)
        return player_index

def handle_client(g,player,lock):
    choice = int(player.recvMsg())
    win_status = 0
    lock.acquire() # lock the game object score
    if g.friend_choice is not None: # expected bug due to race condition
        win_status = checkwin(choice, g.friend_choice)
        if win_status == 0:
            g.broadcast("The game is draw")
            return

        elif win_status == 1:
            username=player.username
            player.sendMsg("You won")
            g.removePlayer(player)
            g.players[0].sendMsg("You lost")
            print(username, "won")
            return

        elif True:
            username=player.username
            player.sendMsg("You lost")
            g.removePlayer(player)
            g.players[0].sendMsg("You won")
            print(username, "lost")
            return

    else:
        g.friend_choice = choice
        lock.release()


def broadcast(msg):
    print("Bradcasting: ", msg)
    for client in g.clients:
        client.send(str(msg).encode())


def handleGame(g):
    """
    Handle the game between two players.

    Args:
        g (Game): The game object containing the two players.
    """
    print("Game started")
    g.player1.sendMsg(f"Game started with {g.player2.username}")
    g.player2.sendMsg(f"Game started with {g.player1.username}")
    lock = threading.Lock()
    threads = []
    for player in g.players:
        thread = threading.Thread(target=handle_client, args=(g, player, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Game ended")
    g.broadcast("Game ended")
    g.broadcast("Waiting for other players")