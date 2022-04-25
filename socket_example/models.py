import socket

class SocketClient(object):
    def __init__(self, host, port, socktype):
        self.host = host
        self.port = port
        self.socktype = socktype

        if self.socktype == 'tcp':
            self._socktype = socket.SOCK_STREAM

        if self.socktype == 'udp':
            self._socktype = socket.SOCK_DGRAM


    def bootstrap(self):
        self.socket = socket.socket(socket.AF_INET, self._socktype)
        self.socket.connect((self.host, self.port))


class SocketServer(object):
    def __init__(self, port, socktype):
        self.port = port
        if socktype == 'tcp':
            self._socktype = socket.SOCK_STREAM

        if socktype == 'udp':
            self._socktype = socket.SOCK_DGRAM

    def bootstrap(self):
        self.socket = socket.socket(socket.AF_INET, self._socktype)
        self.socket.bind(('localhost', self.port))
        self.socket.listen(5)

    def run(self):
        print("Running...")
        while True:
            a, b = self.socket.accept()
            print(f"Received Connection from {b}")