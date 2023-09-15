import socket


def main():
    HOST = input("Enter server address: ")
    PORT = 9090

    # Create a socket connection to the server
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((HOST, PORT))

    # Get user input for username
    username = input("Enter your username: ")
    conn.send(username.encode())

    # Wait for the game to start
    msg = conn.recv(1024).decode()
    print(msg)
    msg = conn.recv(1024).decode()
    print(msg)

    while True:
        # Get user's choice
        print("Enter your choice:")
        print("0: Snake")
        print("1: Water")
        print("2: Gun")
        choice = input("Your choice (0/1/2): ")

        # Send the choice to the server
        conn.send(choice.encode())

        # Receive and print game result
        result = conn.recv(1024).decode()
        print(result)
        break


if __name__ == "__main__":
    main()
