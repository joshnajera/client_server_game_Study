import socket
import pickle

msg = "this is a test"

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.host = "192.168.62.202"
        self.host = "127.0.0.1"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.player = self.connect()
        print("Received player: " , self.player)

    def get_player(self):
        return self.player

    def connect(self):
        """Connects to the game client"""
        try:
            ## Client sockets CONNECT to their given address, instead of binding to them
            self.client.connect(self.addr)
            # loads() unpacks the byte data
            return self.client.recv(2048).decode()
        except:
            print("Could not connect!")
    
    def send(self, player_data):
        """Sends player information to server"""
        try:
            # Send player info (move: ['r','p','s']) to server
            self.client.send(str.encode(player_data))
            # Get other player data from server
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)