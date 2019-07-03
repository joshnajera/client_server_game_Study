import socket
import pickle

msg = "this is a test"

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.62.202"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.player = self.connect()
        print("Received player: " , self.player)
    
    def connect(self):
        try:
            ## Client sockets CONNECT to their given address, instead of binding to them
            self.client.connect(self.addr)
            # loads() unpacks the byte data
            return pickle.loads(self.client.recv(2048))
        except:
            print("Could not connect!")
            pass
    
    def send(self, player_data):
        try:
            # Send player info to server
            self.client.send(pickle.dumps(player_data))
            # Get other player data from server
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def get_player(self):
        return self.player