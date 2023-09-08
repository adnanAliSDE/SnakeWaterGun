import connectivity

def is_valid(username):

    '''Will check the db for available username'''

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
    username=input('Enter your username')
    password=input('Enter your password')

    data={
        "username":username,
        "password":password
    }
    
    connectivity.send_to_server('login',data)