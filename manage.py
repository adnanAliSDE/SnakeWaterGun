import os
import time


def start_server():
    print("Starting the server...")
    os.system("start cmd /k python server.py")


def start_client(username):
    print(f"Starting client for {username}...")
    os.system(f"start cmd /k python client.py && echo localhost && echo {username}")


def main():
    # Start the server
    start_server()
    time.sleep(2)  # Wait for the server to initialize

    # Start two client instances with different usernames
    start_client("user1")
    time.sleep(2)  # Wait for the server to initialize
    start_client("user2")


if __name__ == "__main__":
    main()
