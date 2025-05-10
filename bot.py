# from command import Command
# import numpy as np
# from buttons import Buttons
# import csv

# class Bot:

#     def __init__(self):
#         #< - v + < - v - v + > - > + Y
#         self.fire_code=["<","!<","v+<","!v+!<","v","!v","v+>","!v+!>",">+Y","!>+!Y"]
#         self.exe_code=0
#         self.start_fire=True
#         self.remaining_code=[]
#         self.my_command=Command()
#         self.buttn= Buttons()

#     def fight(self,current_game_state,player):
#         #python Videos\gamebot-competition-master\PythonAPI\controller.py 1
#         if player=="1":
#             #print("1")
#             #v - < + v - < + B spinning

#             if( self.exe_code!=0  ):
#                self.run_command([],current_game_state.player1)
#             diff=current_game_state.player2.x_coord - current_game_state.player1.x_coord
#             if (  diff > 60 ) :
#                 toss=np.random.randint(3)
#                 if (toss==0):
#                     #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
#                     self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
#                 elif ( toss==1 ):
#                     self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player1)
#                 else: #fire
#                     self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
#             elif (  diff < -60 ) :
#                 toss=np.random.randint(3)
#                 if (toss==0):#spinning
#                     #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
#                     self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
#                 elif ( toss==1):#
#                     self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player1)
#                 else: #fire
#                     self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
#             else:
#                 toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
#                 if ( toss>=1 ):
#                     if (diff>0):
#                         self.run_command(["<","<","!<"],current_game_state.player1)
#                     else:
#                         self.run_command([">",">","!>"],current_game_state.player1)
#                 else:
#                     self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player1)
#             self.my_command.player_buttons=self.buttn

#         elif player=="2":

#             if( self.exe_code!=0  ):
#                self.run_command([],current_game_state.player2)
#             diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
#             if (  diff > 60 ) :
#                 toss=np.random.randint(3)
#                 if (toss==0):
#                     #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
#                     self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
#                 elif ( toss==1 ):
#                     self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player2)
#                 else:
#                     self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
#             elif ( diff < -60 ) :
#                 toss=np.random.randint(3)
#                 if (toss==0):
#                     #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
#                     self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
#                 elif ( toss==1):
#                     self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player2)
#                 else:
#                     self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
#             else:
#                 toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
#                 if ( toss>=1 ):
#                     if (diff<0):
#                         self.run_command(["<","<","!<"],current_game_state.player2)
#                     else:
#                         self.run_command([">",">","!>"],current_game_state.player2)
#                 else:
#                     self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player2)
#             self.my_command.player2_buttons=self.buttn
#         return self.my_command



#     def run_command( self , com , player   ):

#         if self.exe_code-1==len(self.fire_code):
#             self.exe_code=0
#             self.start_fire=False
#             print ("compelete")
#             #exit()
#             # print ( "left:",player.player_buttons.left )
#             # print ( "right:",player.player_buttons.right )
#             # print ( "up:",player.player_buttons.up )
#             # print ( "down:",player.player_buttons.down )
#             # print ( "Y:",player.player_buttons.Y )

#         elif len(self.remaining_code)==0 :

#             self.fire_code=com
#             #self.my_command=Command()
#             self.exe_code+=1

#             self.remaining_code=self.fire_code[0:]

#         else:
#             self.exe_code+=1
#             if self.remaining_code[0]=="v+<":
#                 self.buttn.down=True
#                 self.buttn.left=True
#                 print("v+<")
#             elif self.remaining_code[0]=="!v+!<":
#                 self.buttn.down=False
#                 self.buttn.left=False
#                 print("!v+!<")
#             elif self.remaining_code[0]=="v+>":
#                 self.buttn.down=True
#                 self.buttn.right=True
#                 print("v+>")
#             elif self.remaining_code[0]=="!v+!>":
#                 self.buttn.down=False
#                 self.buttn.right=False
#                 print("!v+!>")

#             elif self.remaining_code[0]==">+Y":
#                 self.buttn.Y= True #not (player.player_buttons.Y)
#                 self.buttn.right=True
#                 print(">+Y")
#             elif self.remaining_code[0]=="!>+!Y":
#                 self.buttn.Y= False #not (player.player_buttons.Y)
#                 self.buttn.right=False
#                 print("!>+!Y")

#             elif self.remaining_code[0]=="<+Y":
#                 self.buttn.Y= True #not (player.player_buttons.Y)
#                 self.buttn.left=True
#                 print("<+Y")
#             elif self.remaining_code[0]=="!<+!Y":
#                 self.buttn.Y= False #not (player.player_buttons.Y)
#                 self.buttn.left=False
#                 print("!<+!Y")

#             elif self.remaining_code[0]== ">+^+L" :
#                 self.buttn.right=True
#                 self.buttn.up=True
#                 self.buttn.L= not (player.player_buttons.L)
#                 print(">+^+L")
#             elif self.remaining_code[0]== "!>+!^+!L" :
#                 self.buttn.right=False
#                 self.buttn.up=False
#                 self.buttn.L= False #not (player.player_buttons.L)
#                 print("!>+!^+!L")

#             elif self.remaining_code[0]== ">+^+Y" :
#                 self.buttn.right=True
#                 self.buttn.up=True
#                 self.buttn.Y= not (player.player_buttons.Y)
#                 print(">+^+Y")
#             elif self.remaining_code[0]== "!>+!^+!Y" :
#                 self.buttn.right=False
#                 self.buttn.up=False
#                 self.buttn.Y= False #not (player.player_buttons.L)
#                 print("!>+!^+!Y")


#             elif self.remaining_code[0]== ">+^+R" :
#                 self.buttn.right=True
#                 self.buttn.up=True
#                 self.buttn.R= not (player.player_buttons.R)
#                 print(">+^+R")
#             elif self.remaining_code[0]== "!>+!^+!R" :
#                 self.buttn.right=False
#                 self.buttn.up=False
#                 self.buttn.R= False #ot (player.player_buttons.R)
#                 print("!>+!^+!R")

#             elif self.remaining_code[0]== ">+^+A" :
#                 self.buttn.right=True
#                 self.buttn.up=True
#                 self.buttn.A= not (player.player_buttons.A)
#                 print(">+^+A")
#             elif self.remaining_code[0]== "!>+!^+!A" :
#                 self.buttn.right=False
#                 self.buttn.up=False
#                 self.buttn.A= False #not (player.player_buttons.A)
#                 print("!>+!^+!A")

#             elif self.remaining_code[0]== ">+^+B" :
#                 self.buttn.right=True
#                 self.buttn.up=True
#                 self.buttn.B= not (player.player_buttons.B)
#                 print(">+^+B")
#             elif self.remaining_code[0]== "!>+!^+!B" :
#                 self.buttn.right=False
#                 self.buttn.up=False
#                 self.buttn.B= False #not (player.player_buttons.A)
#                 print("!>+!^+!B")

#             elif self.remaining_code[0]== "<+^+L" :
#                 self.buttn.left=True
#                 self.buttn.up=True
#                 self.buttn.L= not (player.player_buttons.L)
#                 print("<+^+L")
#             elif self.remaining_code[0]== "!<+!^+!L" :
#                 self.buttn.left=False
#                 self.buttn.up=False
#                 self.buttn.L= False  #not (player.player_buttons.Y)
#                 print("!<+!^+!L")

#             elif self.remaining_code[0]== "<+^+Y" :
#                 self.buttn.left=True
#                 self.buttn.up=True
#                 self.buttn.Y= not (player.player_buttons.Y)
#                 print("<+^+Y")
#             elif self.remaining_code[0]== "!<+!^+!Y" :
#                 self.buttn.left=False
#                 self.buttn.up=False
#                 self.buttn.Y= False  #not (player.player_buttons.Y)
#                 print("!<+!^+!Y")

#             elif self.remaining_code[0]== "<+^+R" :
#                 self.buttn.left=True
#                 self.buttn.up=True
#                 self.buttn.R= not (player.player_buttons.R)
#                 print("<+^+R")
#             elif self.remaining_code[0]== "!<+!^+!R" :
#                 self.buttn.left=False
#                 self.buttn.up=False
#                 self.buttn.R= False  #not (player.player_buttons.Y)
#                 print("!<+!^+!R")

#             elif self.remaining_code[0]== "<+^+A" :
#                 self.buttn.left=True
#                 self.buttn.up=True
#                 self.buttn.A= not (player.player_buttons.A)
#                 print("<+^+A")
#             elif self.remaining_code[0]== "!<+!^+!A" :
#                 self.buttn.left=False
#                 self.buttn.up=False
#                 self.buttn.A= False  #not (player.player_buttons.Y)
#                 print("!<+!^+!A")

#             elif self.remaining_code[0]== "<+^+B" :
#                 self.buttn.left=True
#                 self.buttn.up=True
#                 self.buttn.B= not (player.player_buttons.B)
#                 print("<+^+B")
#             elif self.remaining_code[0]== "!<+!^+!B" :
#                 self.buttn.left=False
#                 self.buttn.up=False
#                 self.buttn.B= False  #not (player.player_buttons.Y)
#                 print("!<+!^+!B")

#             elif self.remaining_code[0]== "v+R" :
#                 self.buttn.down=True
#                 self.buttn.R= not (player.player_buttons.R)
#                 print("v+R")
#             elif self.remaining_code[0]== "!v+!R" :
#                 self.buttn.down=False
#                 self.buttn.R= False  #not (player.player_buttons.Y)
#                 print("!v+!R")

#             else:
#                 if self.remaining_code[0] =="v" :
#                     self.buttn.down=True
#                     print ( "down" )
#                 elif self.remaining_code[0] =="!v":
#                     self.buttn.down=False
#                     print ( "Not down" )
#                 elif self.remaining_code[0] =="<" :
#                     print ( "left" )
#                     self.buttn.left=True
#                 elif self.remaining_code[0] =="!<" :
#                     print ( "Not left" )
#                     self.buttn.left=False
#                 elif self.remaining_code[0] ==">" :
#                     print ( "right" )
#                     self.buttn.right=True
#                 elif self.remaining_code[0] =="!>" :
#                     print ( "Not right" )
#                     self.buttn.right=False

#                 elif self.remaining_code[0] =="^" :
#                     print ( "up" )
#                     self.buttn.up=True
#                 elif self.remaining_code[0] =="!^" :
#                     print ( "Not up" )
#                     self.buttn.up=False
#             self.remaining_code=self.remaining_code[1:]
#         return



#Second Code

# from command import Command
# import numpy as np
# from buttons import Buttons
# import csv

# class Bot:

#     def __init__(self):
#         # Initialize fire codes and other variables
#         self.fire_code=["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
#         self.exe_code=0
#         self.start_fire=True
#         self.remaining_code=[]
#         self.my_command=Command()
#         self.buttn=Buttons()

#         # Initialize CSV file for logging
#         self.csv_file="GameData.csv"
#         with open(self.csv_file, mode='w', newline='') as file:
#             writer=csv.writer(file)
#             # Write header: required columns
#             writer.writerow([
#                 'Timer', 'fight result', 'has_round_started', 'is_round_over', 'player1_id', 'player1_health',
#                 'player1_x_coord', 'player1_y_coord', 'player1_is_jumping', 'player1_is_crouching', 'player1_is_player_in_move',
#                 'player1_move_id', 'player1_button_up', 'player1_button_down', 'player1_button_left', 'player1_button_right',
#                 'player1_button_select', 'player1_button_start', 'player1_button_Y', 'player1_button_B', 'player1_button_X', 
#                 'player1_button_A', 'player1_button_L', 'player1_button_R', 'player2_id', 'player2_health', 'player2_x_coord',
#                 'player2_y_coord', 'player2_is_jumping', 'player2_is_crouching', 'player2_is_player_in_move', 'player2_move_id',
#                 'player2_button_up', 'player2_button_down', 'player2_button_left', 'player2_button_right', 'player2_button_select',
#                 'player2_button_start', 'player2_button_Y', 'player2_button_B', 'player2_button_X', 'player2_button_A', 'player2_button_L',
#                 'player2_button_R'
#             ])

#     def fight(self, current_game_state, player):
#         # Extract player 1 details
#         Timer= current_game_state.timer
#         fight_result= current_game_state.fight_result
#         has_round_started= current_game_state.has_round_started
#         is_round_over= current_game_state.is_round_over
#         player1_id= current_game_state.player1.player_id
#         player1_health= current_game_state.player1.health
#         player1_x_coord= current_game_state.player1.x_coord
#         player1_y_coord= current_game_state.player1.y_coord
#         player1_is_jumping= current_game_state.player1.is_jumping
#         player1_is_crouching= current_game_state.player1.is_crouching
#         player1_is_player_in_move= current_game_state.player1.is_player_in_move
#         player1_move_id= current_game_state.player1.move_id
#         player1_button_up= current_game_state.player1.player_buttons.up
#         player1_button_down= current_game_state.player1.player_buttons.down
#         player1_button_left= current_game_state.player1.player_buttons.left
#         player1_button_right= current_game_state.player1.player_buttons.right
#         player1_button_select= current_game_state.player1.player_buttons.select
#         player1_button_start= current_game_state.player1.player_buttons.start
#         player1_button_Y= current_game_state.player1.player_buttons.Y
#         player1_button_B= current_game_state.player1.player_buttons.B
#         player1_button_X= current_game_state.player1.player_buttons.X
#         player1_button_A= current_game_state.player1.player_buttons.A
#         player1_button_L= current_game_state.player1.player_buttons.L
#         player1_button_R= current_game_state.player1.player_buttons.R
#         # Extract player 2 details
#         player2_id= current_game_state.player2.player_id
#         player2_health= current_game_state.player2.health
#         player2_x_coord= current_game_state.player2.x_coord
#         player2_y_coord= current_game_state.player2.y_coord
#         player2_is_jumping= current_game_state.player2.is_jumping
#         player2_is_crouching= current_game_state.player2.is_crouching
#         player2_is_player_in_move= current_game_state.player2.is_player_in_move
#         player2_move_id= current_game_state.player2.move_id
#         player2_button_up= current_game_state.player2.player_buttons.up
#         player2_button_down= current_game_state.player2.player_buttons.down
#         player2_button_left= current_game_state.player2.player_buttons.left
#         player2_button_right= current_game_state.player2.player_buttons.right
#         player2_button_select= current_game_state.player2.player_buttons.select
#         player2_button_start= current_game_state.player2.player_buttons.start
#         player2_button_Y= current_game_state.player2.player_buttons.Y
#         player2_button_B= current_game_state.player2.player_buttons.B
#         player2_button_X= current_game_state.player2.player_buttons.X
#         player2_button_A= current_game_state.player2.player_buttons.A
#         player2_button_L= current_game_state.player2.player_buttons.L
#         player2_button_R= current_game_state.player2.player_buttons.R

       

#         # Write data to CSV
#         with open(self.csv_file, mode='a', newline='') as file:
#             writer=csv.writer(file)
#             writer.writerow([
#                 Timer, fight_result, has_round_started, is_round_over, player1_id, player1_health,
#                 player1_x_coord, player1_y_coord, player1_is_jumping, player1_is_crouching,
#                 player1_is_player_in_move, player1_move_id, player1_button_up, player1_button_down,
#                 player1_button_left, player1_button_right, player1_button_select, player1_button_start,
#                 player1_button_Y, player1_button_B, player1_button_X, player1_button_A,
#                 player1_button_L, player1_button_R,
#                 player2_id, player2_health, player2_x_coord, player2_y_coord,
#                 player2_is_jumping, player2_is_crouching, player2_is_player_in_move,
#                 player2_move_id, player2_button_up, player2_button_down,
#                 player2_button_left, player2_button_right, player2_button_select,
#                 player2_button_start, player2_button_Y, player2_button_B,
#                 player2_button_X, player2_button_A, player2_button_L,
#                 player2_button_R
#             ])


#         # Set the buttons in the command object
#         if player=="1":
#             self.my_command.player_buttons=self.buttn
#         else:
#             self.my_command.player2_buttons=self.buttn

#         return self.my_command

#     def run_command(self, com, player):
#         if self.exe_code - 1 == len(self.fire_code):
#             self.exe_code=0
#             self.start_fire=False
#             print("complete")
#         elif len(self.remaining_code) == 0:
#             self.fire_code=com
#             self.exe_code += 1
#             self.remaining_code=self.fire_code[0:]
#         else:
#             self.exe_code += 1
#             if self.remaining_code[0] == "v+<":
#                 self.buttn.down=True
#                 self.buttn.left=True
#                 print("v+<")
#             elif self.remaining_code[0] == "!v+!<":
#                 self.buttn.down=False
#                 self.buttn.left=False
#                 print("!v+!<")
#             elif self.remaining_code[0] == "v+>":
#                 self.buttn.down=True
#                 self.buttn.right=True
#                 print("v+>")
#             elif self.remaining_code[0] == "!v+!>":
#                 self.buttn.down=False
#                 self.buttn.right=False
#                 print("!v+!>")
#             elif self.remaining_code[0] == ">+Y":
#                 self.buttn.Y=True
#                 self.buttn.right=True
#                 print(">+Y")
#             elif self.remaining_code[0] == "!>+!Y":
#                 self.buttn.Y=False
#                 self.buttn.right=False
#                 print("!>+!Y")
#             elif self.remaining_code[0] == "<+Y":
#                 self.buttn.Y=True
#                 self.buttn.left=True
#                 print("<+Y")
#             elif self.remaining_code[0] == "!<+!Y":
#                 self.buttn.Y=False
#                 self.buttn.left=False
#                 print("!<+!Y")
#             elif self.remaining_code[0] == "v+R":
#                 self.buttn.down=True
#                 self.buttn.R=not player.player_buttons.R
#                 print("v+R")
#             elif self.remaining_code[0] == "!v+!R":
#                 self.buttn.down=False
#                 self.buttn.R=False
#                 print("!v+!R")
#             else:
#                 if self.remaining_code[0] == "v":
#                     self.buttn.down=True
#                     print("down")
#                 elif self.remaining_code[0] == "!v":
#                     self.buttn.down=False
#                     print("Not down")
#                 elif self.remaining_code[0] == "<":
#                     print("left")
#                     self.buttn.left=True
#                 elif self.remaining_code[0] == "!<":
#                     print("Not left")
#                     self.buttn.left=False
#                 elif self.remaining_code[0] == ">":
#                     print("right")
#                     self.buttn.right=True
#                 elif self.remaining_code[0] == "!>":
#                     print("Not right")
#                     self.buttn.right=False
#                 elif self.remaining_code[0] == "^":
#                     print("up")
#                     self.buttn.up=True
#                 elif self.remaining_code[0] == "!^":
#                     print("Not up")
#                     self.buttn.up=False
#             self.remaining_code=self.remaining_code[1:]
#         return



# Fourth Code
# from command import Command
# from game_state import GameState
# from player import Player
# import numpy as np
# import pandas as pd
# from buttons import Buttons
# import sklearn
# from sklearn.preprocessing import StandardScaler
# import joblib
# from tensorflow.keras.models import load_model

# class Bot:

#     def __init__(self):
#         # Initialize fire codes and other variables
#         self.fire_code = ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
#         self.exe_code = 0
#         self.start_fire = True
#         self.remaining_code = []
#         self.my_command = Command()
#         self.buttn = Buttons()

#     def fight(self, current_game_state, player):
#         # Load model and scaler
#         scaler = joblib.load("scaler.joblib")
#         model = load_model("my_model.keras")

#         # Extract features from current_game_state
#         p1Xcoord = current_game_state.player1.x_coord
#         p1Health = current_game_state.player1.health
#         p1Ycoord = current_game_state.player1.y_coord
#         isJumpP1 = current_game_state.player1.is_jumping
#         isCrouchP1 = current_game_state.player1.is_crouching
#         p1PlayerId = current_game_state.player1.player_id
#         P1InMove = current_game_state.player1.is_player_in_move
#         P1MoveId = current_game_state.player1.move_id

#         p2Xcoord = current_game_state.player2.x_coord
#         p2Health = current_game_state.player2.health
#         p2Ycoord = current_game_state.player2.y_coord
#         isJumpP2 = current_game_state.player2.is_jumping
#         isCrouchP2 = current_game_state.player2.is_crouching
#         p2PlayerId = current_game_state.player2.player_id
#         P2InMove = current_game_state.player2.is_player_in_move
#         P2MoveId = current_game_state.player2.move_id

#         timer = current_game_state.timer
#         RoundStart = current_game_state.has_round_started
#         RoundOver = current_game_state.is_round_over

#         # Compute additional features
#         delta_p1_health = 15
#         delta_p2_health = 0 
#         delta_distance = ((p1Xcoord - p2Xcoord)**2 + (p1Ycoord - p2Ycoord)**2) ** 0.5

#         # Construct the feature vector with all 22 features
#         features = pd.DataFrame([[
#                 p1Xcoord, p1Health, p1Ycoord, isJumpP1, isCrouchP1,
#                 p2Xcoord, p2Health, p2Ycoord, isJumpP2, isCrouchP2,
#                 p1PlayerId, P1InMove, P1MoveId, p2PlayerId, P2InMove, P2MoveId,
#                 timer, RoundStart, RoundOver,
#                 delta_p1_health, delta_p2_health, delta_distance
#             ]])

#         # Scale the features
#         features_scaled = scaler.transform(features)
#         SolPredVa = model.predict(features_scaled)

#         # Update button states based on predictions
#         if player == "1":
#                 self.buttn.up = int(SolPredVa[0][0])
#                 self.buttn.down = int(SolPredVa[0][1])
#                 self.buttn.right = int(SolPredVa[0][2])
#                 self.buttn.left = int(SolPredVa[0][3])
#                 self.buttn.X = int(SolPredVa[0][4])
#                 self.buttn.Y = int(SolPredVa[0][5])
#                 self.buttn.A = int(SolPredVa[0][6])
#                 self.buttn.B = int(SolPredVa[0][7])
#                 self.buttn.L = int(SolPredVa[0][8])
#                 self.buttn.R = int(SolPredVa[0][9])
#                 self.my_command.player_buttons = self.buttn

#         elif player == "2":
#                 self.buttn.up = int(SolPredVa[0][0])
#                 self.buttn.down = int(SolPredVa[0][1])
#                 self.buttn.right = int(SolPredVa[0][2])
#                 self.buttn.left = int(SolPredVa[0][3])
#                 self.buttn.X = int(SolPredVa[0][4])
#                 self.buttn.Y = int(SolPredVa[0][5])
#                 self.buttn.A = int(SolPredVa[0][6])
#                 self.buttn.B = int(SolPredVa[0][7])
#                 self.buttn.L = int(SolPredVa[0][8])
#                 self.buttn.R = int(SolPredVa[0][9])
#                 self.my_command.player2_buttons = self.buttn  # Corrected to player2_buttons

#         return self.my_command

#     def run_command(self, com, player):
#         if self.exe_code - 1 == len(self.fire_code):
#             self.exe_code = 0
#             self.start_fire = False
#             print("complete")
#         elif len(self.remaining_code) == 0:
#             self.fire_code = com
#             self.exe_code += 1
#             self.remaining_code = self.fire_code[0:]
#         else:
#             self.exe_code += 1
#             if self.remaining_code[0] == "v+<":
#                 self.buttn.down = True
#                 self.buttn.left = True
#                 print("v+<")
#             elif self.remaining_code[0] == "!v+!<":
#                 self.buttn.down = False
#                 self.buttn.left = False
#                 print("!v+!<")
#             elif self.remaining_code[0] == "v+>":
#                 self.buttn.down = True
#                 self.buttn.right = True
#                 print("v+>")
#             elif self.remaining_code[0] == "!v+!>":
#                 self.buttn.down = False
#                 self.buttn.right = False
#                 print("!v+!>")
#             elif self.remaining_code[0] == ">+Y":
#                 self.buttn.Y = True
#                 self.buttn.right = True
#                 print(">+Y")
#             elif self.remaining_code[0] == "!>+!Y":
#                 self.buttn.Y = False
#                 self.buttn.right = False
#                 print("!>+!Y")
#             elif self.remaining_code[0] == "<+Y":
#                 self.buttn.Y = True
#                 self.buttn.left = True
#                 print("<+Y")
#             elif self.remaining_code[0] == "!<+!Y":
#                 self.buttn.Y = False
#                 self.buttn.left = False
#                 print("!<+!Y")
#             elif self.remaining_code[0] == "v+R":
#                 self.buttn.down = True
#                 self.buttn.R = not player.player_buttons.R
#                 print("v+R")
#             elif self.remaining_code[0] == "!v+!R":
#                 self.buttn.down = False
#                 self.buttn.R = False
#                 print("!v+!R")
#             else:
#                 if self.remaining_code[0] == "v":
#                     self.buttn.down = True
#                     print("down")
#                 elif self.remaining_code[0] == "!v":
#                     self.buttn.down = False
#                     print("Not down")
#                 elif self.remaining_code[0] == "<":
#                     print("left")
#                     self.buttn.left = True
#                 elif self.remaining_code[0] == "!<":
#                     print("Not left")
#                     self.buttn.left = False
#                 elif self.remaining_code[0] == ">":
#                     print("right")
#                     self.buttn.right = True
#                 elif self.remaining_code[0] == "!>":
#                     print("Not right")
#                     self.buttn.right = False
#                 elif self.remaining_code[0] == "^":
#                     print("up")
#                     self.buttn.up = True
#                 elif self.remaining_code[0] == "!^":
#                     print("Not up")
#                     self.buttn.up = False
#             self.remaining_code = self.remaining_code[1:]
#         return


#Final
from command import Command
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from buttons import Buttons
import joblib
from collections import namedtuple

# Define a namedtuple for clarity
GameStateInput = namedtuple("GameStateInput", [
    "timer", "p2_health", "p2_x", "p2_y",
    "p1_x", "p1_y", "p1_jumping", "p1_crouching",
    "x_diff", "y_diff"
])


class Bot:

    def __init__(self):
        self.fire_code = ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
        self.exe_code = 0
        self.start_fire = True
        self.remaining_code = []
        self.my_command = Command()
        self.buttn = Buttons()
        self.bot_model = tf.keras.models.load_model('BotModel.h5')
        self.scaler = joblib.load('scaler.save')
        self.button_names = ['up', 'down', 'left', 'right', 'L', 'R', 'A', 'X', 'B', 'Y']

    def set_buttons_false(self):
        for button in self.button_names:
            setattr(self.buttn, button, False)

    def extract_features(self, state):
        return GameStateInput(
            timer=state.timer,
            p2_health=state.player2.health,
            p2_x=state.player2.x_coord,
            p2_y=state.player2.y_coord,
            p1_x=state.player1.x_coord,
            p1_y=state.player1.y_coord,
            p1_jumping=state.player1.is_jumping,
            p1_crouching=state.player1.is_crouching,
            x_diff=abs(state.player1.x_coord - state.player2.x_coord),
            y_diff=abs(state.player1.y_coord - state.player2.y_coord)
        )

    def get_scaled_input(self, game_state):
        features = self.extract_features(game_state)
        return self.scaler.transform([list(features)])

    def predict_buttons(self, scaled_input):
        predictions = self.bot_model.predict(scaled_input)
        return (predictions > 0.1)[0]

    def apply_predictions_to_buttons(self, prediction_vector):
        self.set_buttons_false()
        for i, active in enumerate(prediction_vector):
            setattr(self.buttn, self.button_names[i], bool(active))

    def fight(self, current_game_state, player):
        if player == "1":
            scaled_input = self.get_scaled_input(current_game_state)
            prediction_vector = self.predict_buttons(scaled_input)
            self.apply_predictions_to_buttons(prediction_vector)
            self.my_command.player_buttons = self.buttn
        elif player == "2":
            self.my_command.player2_buttons = self.buttn

        return self.my_command


#Final1
# from command import Command
# import numpy as np
# import tensorflow as tf
# from sklearn.preprocessing import StandardScaler
# from buttons import Buttons
# import joblib


# class Bot:

#     def __init__(self):
#         self.fire_code = ["<", "!<", "v+<", "!v+!<", "v", "!v", "v+>", "!v+!>", ">+Y", "!>+!Y"]
#         self.exe_code = 0
#         self.start_fire = True
#         self.remaining_code = []
#         self.my_command = Command()
#         self.buttn = Buttons()
#         self.bot_model = tf.keras.models.load_model('BotModel.h5')
#         self.scaler = joblib.load('scaler.save')


#     def setButtonsFalse(self):

#         self.buttn.up = False
#         self.buttn.down = False
#         self.buttn.left = False
#         self.buttn.right = False
#         self.buttn.L = False
#         self.buttn.R = False
#         self.buttn.A = False
#         self.buttn.B = False
#         self.buttn.X = False
#         self.buttn.Y = False

#     def fight(self, current_game_state, player):

#         if player == "1":

#             single_input = np.array([[current_game_state.timer, current_game_state.player2.health, current_game_state.player2.x_coord, current_game_state.player2.y_coord, current_game_state.player1.x_coord,	current_game_state.player1.y_coord,	current_game_state.player1.is_jumping,	current_game_state.player1.is_crouching, abs(current_game_state.player1.x_coord-current_game_state.player1.x_coord), abs(current_game_state.player1.y_coord-current_game_state.player1.y_coord)]])

#             scaled_input = self.scaler.transform(single_input)

#             predictions = self.bot_model.predict(scaled_input)
#             predicted_buttons = (predictions > 0.1)
#             predicted_buttons = predicted_buttons.astype(bool)

#             self.setButtonsFalse()
#             if predicted_buttons[0][0]:
#                 self.buttn.up = True

#             if predicted_buttons[0][1]:
#                 self.buttn.down = True

#             if predicted_buttons[0][2]:
#                 self.buttn.left = True

#             if predicted_buttons[0][3]:
#                 self.buttn.right = True

#             if predicted_buttons[0][4]:
#                 self.buttn.L = True

#             if predicted_buttons[0][5]:
#                 self.buttn.R = True

#             if predicted_buttons[0][6]:
#                 self.buttn.A = True

#             if predicted_buttons[0][7]:
#                 self.buttn.X = True

#             if predicted_buttons[0][8]:
#                 self.buttn.B = True

#             if predicted_buttons[0][9]:
#                 self.buttn.Y = True

#             self.my_command.player_buttons = self.buttn

#         elif player == "2":
#             self.my_command.player2_buttons = self.buttn

#         return self.my_command
