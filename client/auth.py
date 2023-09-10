import connectivity


def is_valid(username):
    """Will check the db for available username"""
    is_available = False
    context = {"username": username}
    status, res = connectivity.send_data("is_valid_username", context)
    is_available = bool(res)
    return is_available


def createAccount():
    username = ""
    while True:
        username = input("Choose a username: ")
        if is_valid(username):
            break

        else:
            print("Username not available please try another one")

    password = input("Enter your password: ")
    context = {"username": username, "password": password}

    sent, res = connectivity.send_data("create_account", context)

    if sent:
        print("Account created successfully")
        handleLogin()
        return
    else:
        print(res)
        createAccount()


def handleLogin():
    username = input("Enter your username")
    password = input("Enter your password")

    data = {"username": username, "password": password}

    is_authenticated = False
    _, res = connectivity.send_to_server("login", data)
    is_authenticated = bool(res)

    if is_authenticated:
        return is_authenticated
    else:
        handleLogin()
