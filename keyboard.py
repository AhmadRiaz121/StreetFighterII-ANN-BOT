import socket
import json
from game_state import GameState
import sys
from command import Command
from buttons import Buttons
from pynput import keyboard
import threading
import pandas as pd
import os

# Dictionary to track the state of keyboard keys
key_states = {
    'w': False,  # up
    's': False,  # down
    'a': False,  # left
    'd': False,  # right
    'u': False,  # Y
    'i': False,  # B
    'o': False,  # X
    'j': False,  # A
    'k': False,  # L
    'l': False,  # R
    'return': False,  # select
    'space': False,  # start
}

# List to store game state data
game_data = []

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char in key_states:
            key_states[key.char] = True
        elif key == keyboard.Key.enter:
            key_states['return'] = True
        elif key == keyboard.Key.space:
            key_states['space'] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if hasattr(key, 'char') and key.char in key_states:
            key_states[key.char] = False
        elif key == keyboard.Key.enter:
            key_states['return'] = False
        elif key == keyboard.Key.space:
            key_states['space'] = False
    except AttributeError:
        pass

def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    return listener

def update_buttons_from_keyboard(buttons):
    buttons.up = key_states['w']
    buttons.down = key_states['s']
    buttons.left = key_states['a']
    buttons.right = key_states['d']
    buttons.Y = key_states['u']
    buttons.B = key_states['i']
    buttons.X = key_states['o']
    buttons.A = key_states['j']
    buttons.L = key_states['k']
    buttons.R = key_states['l']
    buttons.select = key_states['return']
    buttons.start = key_states['space']

def connect(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))
    server_socket.listen(5)
    (client_socket, _) = server_socket.accept()
    print("Connected to game!")
    return client_socket

def send(client_socket, command):
    command_dict = command.object_to_dict()
    pay_load = json.dumps(command_dict).encode()
    client_socket.sendall(pay_load)

def receive(client_socket):
    pay_load = client_socket.recv(4096)
    input_dict = json.loads(pay_load.decode())
    game_state = GameState(input_dict)
    return game_state

def log_game_state(game_state):
    data = {
        'Timer': game_state.timer,
        'fight result': game_state.fight_result,
        'has_round_started': game_state.has_round_started,
        'is_round_over': game_state.is_round_over,
        'player1_id': game_state.player1.player_id,
        'player1_health': game_state.player1.health,
        'player1_x_coord': game_state.player1.x_coord,
        'player1_y_coord': game_state.player1.y_coord,
        'player1_is_jumping': game_state.player1.is_jumping,
        'player1_is_crouching': game_state.player1.is_crouching,
        'player1_is_player_in_move': game_state.player1.is_player_in_move,
        'player1_move_id': game_state.player1.move_id,
        'player1_button_up': game_state.player1.player_buttons.up,
        'player1_button_down': game_state.player1.player_buttons.down,
        'player1_button_left': game_state.player1.player_buttons.left,
        'player1_button_right': game_state.player1.player_buttons.right,
        'player1_button_select': game_state.player1.player_buttons.select,
        'player1_button_start': game_state.player1.player_buttons.start,
        'player1_button_Y': game_state.player1.player_buttons.Y,
        'player1_button_B': game_state.player1.player_buttons.B,
        'player1_button_X': game_state.player1.player_buttons.X,
        'player1_button_A': game_state.player1.player_buttons.A,
        'player1_button_L': game_state.player1.player_buttons.L,
        'player1_button_R': game_state.player1.player_buttons.R,
        'player2_id': game_state.player2.player_id,
        'player2_health': game_state.player2.health,
        'player2_x_coord': game_state.player2.x_coord,
        'player2_y_coord': game_state.player2.y_coord,
        'player2_is_jumping': game_state.player2.is_jumping,
        'player2_is_crouching': game_state.player2.is_crouching,
        'player2_is_player_in_move': game_state.player2.is_player_in_move,
        'player2_move_id': game_state.player2.move_id,
        'player2_button_up': game_state.player2.player_buttons.up,
        'player2_button_down': game_state.player2.player_buttons.down,
        'player2_button_left': game_state.player2.player_buttons.left,
        'player2_button_right': game_state.player2.player_buttons.right,
        'player2_button_select': game_state.player2.player_buttons.select,
        'player2_button_start': game_state.player2.player_buttons.start,
        'player2_button_Y': game_state.player2.player_buttons.Y,
        'player2_button_B': game_state.player2.player_buttons.B,
        'player2_button_X': game_state.player2.player_buttons.X,
        'player2_button_A': game_state.player2.player_buttons.A,
        'player2_button_L': game_state.player2.player_buttons.L,
        'player2_button_R': game_state.player2.player_buttons.R,
    }
    game_data.append(data)

def save_game_data():
    df = pd.DataFrame(game_data)
    filename = 'GameData.csv'
    file_exists = os.path.isfile(filename)
    df.to_csv(filename, mode='a', header=not file_exists, index=False)
    print(f"Appended game data to {filename}")

def main():
    if sys.argv[1] == '1':
        client_socket = connect(9999)
    elif sys.argv[1] == '2':
        client_socket = connect(10000)
    else:
        print("Invalid player number. Use '1' or '2'.")
        return

    listener = start_keyboard_listener()
    current_game_state = None
    command = Command()
    global game_data
    game_data = []  # Initialize game_data

    while (current_game_state is None) or (not current_game_state.is_round_over):
        current_game_state = receive(client_socket)
        log_game_state(current_game_state)  # Log game state data

        if sys.argv[1] == '1':
            update_buttons_from_keyboard(command.player_buttons)
        elif sys.argv[1] == '2':
            update_buttons_from_keyboard(command.player2_buttons)

        send(client_socket, command)

    # Save data when the round is over
    save_game_data()

    listener.stop()
    client_socket.close()

if __name__ == '__main__':
    main()