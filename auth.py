def is_valid(username):
    if username != "computer":
        return True
    else:
        return False


def createAccount():
    username = ""
    while True:
        username = input("Choose a username: ")
        if is_valid(username):
            break

        else:
            print("Username not available please try another one")

    password = input("Enter your password")

def handleLogin():
    print("I am handleLogin")
