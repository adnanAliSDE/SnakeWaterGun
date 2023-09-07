"""
This is an updated version of swg previously made during daysofpython 
"""
import auth
import socket

c = socket.socket()
# Asking for options
def play():
    print("I am play")


def welcome():
    """Take user input for the option to continue next"""

    print("Choose an option to continue\n")
    print("1- Create an account")
    print("2- Login")
    print("3- Play as guest")
    print("4- Exit\n")

    userInp = int(input("Please select your choice: "))
    print(userInp)

    match userInp:
        case 1:
            auth.createAccount()

        case 2:
            auth.handleLogin()

        case 3:
            play()

        case 4:
            print("Thank you for choosing to play SnakeWaterGun")
            return

        case _:
            print("Please provide a valid choice")
            welcome()


try:
    c.connect(("localhost", 9090))
    print("connected to localhost")
    welcome()
except:
    print("Connection failed to server please restart the game")

c.close()

print("Disconnected")
