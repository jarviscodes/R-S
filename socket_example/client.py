from models import SocketClient

x = SocketClient('localhost', 2048, 'tcp')
x.bootstrap()

