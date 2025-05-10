import socket
import json
from game_state import GameState
#from bot import fight
import sys
from bot import Bot


def connect(port):
    #For making a connection with the game
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print ("Connected to game!")
    return client_socket

def send(client_socket, command):
    #This function will send your updated command to Bizhawk so that game reacts according to your command.
    command_dict = command.object_to_dict()
    pay_load = json.dumps(command_dict).encode()
    client_socket.sendall(pay_load)

def receive(client_socket):
    #receive the game state and return game state
    pay_load = client_socket.recv(4096)
    input_dict = json.loads(pay_load.decode())
    game_state = GameState(input_dict)
    return game_state


def main():
    if sys.argv[1] == '1':
        client_socket = connect(9999)
    elif sys.argv[1] == '2':
        client_socket = connect(10000)
    current_game_state = None
    bot = Bot()
    while (current_game_state is None) or (not current_game_state.is_round_over):

        current_game_state = receive(client_socket)
        bot_command = bot.fight(current_game_state, sys.argv[1])
        send(client_socket, bot_command)

        if current_game_state is not None:

            if current_game_state.player2.player_buttons.up:
                print('Up')
            if current_game_state.player2.player_buttons.down:
                print('Down')
            if current_game_state.player2.player_buttons.left:
                print('Left')
            if current_game_state.player2.player_buttons.right:
                print('Right')

            if current_game_state.player2.player_buttons.L:
                print('L')
            if current_game_state.player2.player_buttons.R:
                print('R')
            if current_game_state.player2.player_buttons.A:
                print('A')
            if current_game_state.player2.player_buttons.B:
                print('B')

            if current_game_state.player2.player_buttons.X:
                print('X')
            if current_game_state.player2.player_buttons.Y:
                print('Y')

if __name__ == '__main__':
    main()
