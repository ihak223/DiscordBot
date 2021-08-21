import threading
import socket

ip = "192.168.1.127"

class Client:
    def __init__(self):


class Server:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
