"""
take client and handle them
"""
import game
import matching
import threading
import socket

HOST = "0.0.0.0"
PORT = 8080

s = socket.socket()
s.bind((HOST, PORT))

s.listen(50)
print(f"Listening on PORT: {PORT}...")

# Main logic
"""Take client
ask username
Send welcome
call matching algorithm
send waiting message
"""

while True:
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    username = conn.recv(1024).decode()
    conn.send(f"Welcome {username} to Snake Water Gun".encode())
    
    print(f"{addr} username: {username}")
    player = game.Player(username, conn)
    lock=threading.Lock()
    t = threading.Thread(target=matching.match_players, args=(player,lock))
    t.daemon = True
    t.start()
    conn.send("Waiting for opponent...".encode())