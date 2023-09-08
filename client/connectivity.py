import socket

c = socket.socket()

def connect_to_server(HOST, PORT):
    try:
        c.connect((HOST, PORT))
        return c
    except:
        return False


def send_data(endpoint, data):
    msg = [
        endpoint, data
    ]
    c.send(str(msg).encode())

    res=c.recv(1024).decode()
    return res