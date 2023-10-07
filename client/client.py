import socket

HOST = input("Enter server doamin/IP: ")
PORT = int(input("Enter server port: "))

c=socket.socket()

try:
    c.connect((HOST,PORT))
except:
    print("Connection error Please restart the game")
    exit(0)


# utilty functions
def updateScore(msg):
    gained_score=0
    if msg=="You won":
        gained_score=1

    with open("score.txt",'w+') as f:
        try:
            score=int(f.read())
            score+=gained_score
            f.write(str(score))
            return score

        except:
            f.write(str(gained_score))
            return gained_score

# main logic
username = input("Enter username: ")
c.send(username.encode())

msg=''
while True:
    msg=c.recv(1024).decode()
    print(msg)
    if "Game started with" in msg:
        break


options=['Snake','Water','Gun']
for i in range(3):
    print(f"{i}. {options[i]}")
    
i=int(input("Enter choice (0/1/2): "))
c.send(str(i).encode())

winMsg=c.recv(1024).decode()

score=updateScore(winMsg)
print(f"Your total score: {score}")
print(winMsg)
print("Game ended")

c.close()
print("Connection closed")
