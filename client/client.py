"""
This is an updated version of swg previously made during 100daysofpython 
"""
import auth
import connectivity

conn = None
while True:
    HOST = input("Enter server address: ")
    PORT = int(input("Enter PORT no: "))
    conn = connectivity.connect_to_server(HOST, PORT)
    if conn:
        break
    else:
        print("Connection to server failed Please try again\n")

print("Connected successfully")


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
            is_logged_in = auth.handleLogin()
            if is_logged_in:
                play()

            else:
                print("Please try to login again")
                auth.handleLogin()

        case 3:
            play()

        case 4:
            print("Thank you for choosing to play SnakeWaterGun")
            return

        case _:
            print("Please provide a valid choice")
            welcome()

welcome()
conn.close()
print("Disconnected")