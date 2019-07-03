import socket

msg = "this is a test"

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.62.202"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.pos = self.connect()
        print("Received position: " , self.pos)
    
    def connect(self):
        try:
            ## Client sockets CONNECT to their given address, instead of binding to them
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            print("Could not connect!")
            pass
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def getPos(self):
        return self.pos 


# n = Network()
# print(n.send("asdf"))
# print(n.send("asdf22"))
# print(n.send("asdf55"))