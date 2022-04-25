from models import SocketServer

x = SocketServer(2048, 'tcp')
x.bootstrap()
x.run()



