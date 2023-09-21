import socket

def updateScore(points):
    score = 0
    with open("score.txt", "w+") as f:
        if f.read() != "":
            score = int(f.read())
        score += points
        f.write(str(score))

    return score


def main():
    """
    Establishes a socket connection with a server, sends and receives messages, and allows the user to play a game by making choices and receiving game results.
    """
    HOST = input("Enter server address: ")
    PORT = 9090

    try:
        # Create a socket connection to the server
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((HOST, PORT))
    except Exception as e:
        print(f"An error occurred while connecting to the server: {e}")
        return

    # Get user input for username
    username = input("Enter your username: ")
    conn.send(username.encode())

    # Wait for the game to start
    msg = ""
    while "Game started with" not in msg:
        msg = conn.recv(1024).decode()
        print(msg)

    options = {0: "Snake", 1: "Water", 2: "Gun"}

    # Get user's choice
    print("Enter your choice:")
    for key, value in options.items():
        print(f"{key}: {value}")

    choice = input("Your choice (0/1/2): ")
    # Send the choice to the server
    conn.send(choice.encode())

    # Receive and print game result
    result = conn.recv(1024).decode()
    print(result)

    score=0
    if result=='You won':
        score+=1
    new_score = updateScore(score)
    print("Your score: ", score)
    print("Total score earned: ", new_score)


if __name__ == "__main__":
    main()
