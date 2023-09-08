import socket

c = socket.socket()


def connect_to_server(HOST: str, PORT: int) -> socket.socket:
    """
    Establishes a connection to a server using a socket.

    Args:
        HOST (str): The host address of the server.
        PORT (int): The port number of the server.

    Returns:
        socket.socket: The socket object if the connection is successful, False otherwise.
    """
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((HOST, PORT))
        return c
    except Exception:
        return False


def send_data(endpoint, data):
    msg = [endpoint, data]
    c.send(str(msg).encode())

    sent = bool(c.recv(1024).decode())
    res = c.recv(1024).decode()
    return sent, res