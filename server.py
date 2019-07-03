import socket
from _thread import *
import sys

player_positions = [(0, 0), (100, 100)]
current_player = 0

def threaded_client(conn, player):
    # Send starting position
    conn.send(str.encode(make_pos(player_positions[player])))
    reply = ""

    while True:
        try:
            # Receive up to 2048 bits of information
            # Get player's position and update
            data = conn.recv(2048).decode()
            player_positions[player] = read_pos(data)

            if not data:
                print("Disconnected from client!")
                break

            # Send other player's position
            if player == 1:
                reply = player_positions[0]
            else:
                reply = player_positions[1]
            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()


def read_pos(str):
    """Convert string to a position tuple"""
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    """Converts tuple to a string as 'x,y' """
    return str(tup[0]) + "," + str(tup[1])


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
