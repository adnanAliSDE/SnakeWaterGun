import socket
import threading
from algorithms import game
from algorithms import matching

s = socket.socket()

try:
    s.bind(("0.0.0.0", 9090))
except OSError as e:
    print(f"Error binding to the socket: {e}")
    exit(1)

s.listen(10)
print("listening at port 9090")

class Player:
	def __init__(self,conn,addr,username):
		pass

class Game:
    def __init__(self):
        self.clients = []
        self.usernames = []
        self.friend_choice = None

    def is_client_matched(self):
        if len(self.clients) % 2 == 0:
            return True
        else:
            return False


g = Game()


def handle_client(conn):
    choice = conn.recv(1024).decode()
    choice = int(choice)

    win_status = 0
    if g.friend_choice is not None:
        win_status = game.checkwin(choice, g.friend_choice)
        if win_status == 0:
            broadcast("The game is draw")
            return

        elif win_status == 1:
            index=g.clients.index(conn)
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


while True:
    conn, addr = s.accept()
    g.clients.append(conn)
    username = conn.recv(1024).decode()
    g.usernames.append(username)

    conn.send(f"Welcome {username} to SWG\n".encode())
    conn.send("Please wait until your friend joins\n".encode())
    conn.send("".encode())


    # 2-send alert
    if g.is_client_matched():
        print("Matched")
        g.clients[0].send(f"Game started with {g.usernames[1]}\n".encode())
        g.clients[1].send(f"Game started with {g.usernames[0]}\n".encode())

        for c in g.clients:
            client_handler = threading.Thread(target=handle_client, args=(c,))
            client_handler.start()
        print("Message sent and handling threads")
    else:
        continue
