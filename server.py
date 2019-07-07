import socket
from _thread import *
import sys
from player import player
import pickle
from game import game

connect_clients = set()
games = dict()  # {id:game}
id_count = 0

host = ""
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    str(e)


def threaded_client(conn, player, game_id):
    """Represents a server for players to play on"""
    global id_count
    conn.send(str.encode(str(player)))
    reply = ""
    try:
        while True:
            data = conn.recv(4096).decode()
            game = games[game_id]
            if not data:
                break  # Error out
            if data == "reset":
                game.reset()
            elif data != "get":
                game.play(p, data)
            else:
                reply = game
                conn.sendall(pickle.dumps(reply))
    except:
        pass
    print("Connection lost")
    try:
        del games[game_id]
        print("Closing game", game_id)
    except:
        pass
    id_count -= 1
    conn.close()


s.listen()
print("Waiting for a connection, server started")

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    id_count += 1
    p = 0
    game_id = (id_count - 1) // 2

    # Unpaired player exists
    if game_id % 2 == 1:
        games[game_id] = game(game_id)
        print("creating a new game")

    # Player pair exists
    else:
        games[game_id].ready = True
        p = 1

    # Spin up a new thread to handle the connection
    start_new_thread(threaded_client, (conn, p, game_id))
