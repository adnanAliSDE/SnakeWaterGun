# 1-will listen
import socket
import threading
import game

s = socket.socket()
s.bind(("0.0.0.0", 9090))

s.listen(2)
print("listening at port 9090")


clients = []
usernames = []
friend_choice = None


def handle_client(conn):
    global friend_choice
    choice = conn.recv(1024).decode()
    choice = int(choice)
    win_status = 0
    if friend_choice is not None:
        win_status = game.checkwin(choice, friend_choice)
        if win_status == 0:
            broadcast("The game is draw")

        elif win_status == 1:
            conn.send(f"You won".encode())
            clients.remove(conn)
            broadcast("You lost")
            print(username[0], "lost")

    else:
        friend_choice = choice


def broadcast(msg):
    for client in clients:
        client.send(str(msg).encode())


while True:
    conn, addr = s.accept()
    clients.append(conn)
    username = conn.recv(1024).decode()
    usernames.append(username)

    conn.send(f"Welcome {username} to SWG\n".encode())
    conn.send("Please wait until your friend joins\n".encode())
    conn.send("".encode())

    # 2-send alert
    if len(clients) == 2:
        clients[0].send(f"Game started with {usernames[1]}\n".encode())
        clients[1].send(f"Game started with {usernames[0]}\n".encode())
        for c in clients:
            client_handler = threading.Thread(target=handle_client, args=(c,))
            client_handler.start()
    else:
        continue
