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

# main logic



# handling client connections
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
