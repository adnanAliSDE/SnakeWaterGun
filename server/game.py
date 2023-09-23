import threading

options = ["snake", "water", "gun"]
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
    
    def removePlayer(self,player)


def handle_client(g,player):
    choice = int(player.recvMsg())
    win_status = 0
    if g.friend_choice is not None: # expected bug
        win_status = checkwin(choice, g.friend_choice)
        if win_status == 0:
            g.broadcast("The game is draw")
            return

        elif win_status == 1:
            index=g.players.index(player)
            conn.send(f"You won".encode())

            g.clients.pop(index)
            g.usernames.pop(index)

            broadcast("You lost")
            print(g.usernames[0], "lost")
            return

        elif True:
            index=g.clients.index(conn)
            conn.send(f"You lost".encode())

            username=g.usernames[index]
            g.clients.pop(index)
            g.usernames.pop(index)

            broadcast("You won")
            print(username, "lost")
            return

    else:
        g.friend_choice = choice


def broadcast(msg):
    print("Bradcasting: ", msg)
    for client in g.clients:
        client.send(str(msg).encode())


def handleGame(g):
    