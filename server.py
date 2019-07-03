import socket
from _thread import *
import sys
from player import player
import pickle

players = [player(0,0,50,50,(0,128,0)), player(0,0,50,50,(128,0,0))]
current_player = 0

def threaded_client(conn, player):
    # Send starting position
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            # Get player's position and update
            data = conn.recv(2048)
            players[player] = pickle.loads(data)

            # No data? Disconnected
            if not data:
                print("Disconnected from client!")
                break

            # Connection maintained: Send other player's position
            if player == 1:
                reply = players[0]
            else:
                reply = players[1]
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()



# host = "192.168.62.202"
host = ""
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOCK_STREAM ==> TCP
# SOCK_DGRAM ==> UDP

# AF means Address Family
# INET means IPv4

try:
    # Servers sockets BIND their given address, instead of connecting to them
    s.bind((host, port))
except socket.error as e:
    str(e)

# Servers then listen for connections
s.listen(2)  # Listen, limiting the number of connections
print("Waiting for a connection, server started")

while True:
    # Servers must accept connections from listening socket
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # Spin up a new thread to handle the connection
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
