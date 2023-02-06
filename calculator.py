import math
import random
#Asking for player name and printing it
print("Fifa 23 Card Creator")
player = input("What is the players name? ")
print(f"Player Name: {player}")

#asking for positioning of the player
list2 = ["LB","RB","CB","LWB","RWB","CDM","CM","CAM","LM","RM","LW","RW","CF","ST"]
def position(list2):
  print("LB,RB,CB,LWB,RWB,CDM,CM,CAM,LM,RM,LW,RW,CF,ST")
  position1 = input("What position do want him to be? The positions are listed above↑").upper()
  if position1 not in list2:
    print("Sorry pick a position from the list above?")
    return position(list2)
  else:
    print(f"Player Position: {position1}")

list1=list(range(10,100))
# Will calculate the pace of the player
def pace(list1):
  print("Enter a number from 10 - 99, the higher the number is the higher the overall will be!")
  acceleration = int(input("Acceleration: "))
  sprint_speed = int(input("Sprint Speed: "))
  pace1 = round((acceleration + sprint_speed) / 2)
  if acceleration and sprint_speed not in list1:
    print("Sorry pick a number from 10-99!")
    return pace(list1)
  else:
   print(f"Your player's shooting: {pace1} ")


  # Shooting
def shooting(list1):
  att_postioning = int(input("Att.Positioning: "))
  finishing = int(input("Finishing: "))
  shot_power = int(input("Shot Power: "))
  long_shots = int(input("Long Shots: "))
  volleys = int(input("Volleys: "))
  penalties = int(input("Penalties: "))
  #shooting1 = round((att_postioning + finishing + shot_power+ long_shots+ volleys + penalties) / 6)
  if att_postioning and finishing and shot_power and long_shots and volleys and penalties not in list1:
    print("Sorry pick a number from 10-99!")
    return shooting(list1)
  else:
    shooting1 = round((att_postioning + finishing + shot_power+ long_shots+ volleys + penalties)/6)
    print(f"Your player's pace: {shooting1} ")


  # Passing
#def passing():




  # Dribbling
dribbling_list = [] 
max_length = 6

def dribbling_stats(dribbling_list, max_length, sum):
  dribbling_input = int(input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order."))
  while len(dribbling_list) <= max_length:
    dribbling_list.append(dribbling_input)
  print(f"Your dribbling inputs: {dribbling_list} ")
  sum = dribbling_list(sum)
  final_dribbling = sum/2
  print(f"Your player's final dribbling stat: {final_dribbling} ")
  while False: 
    print("Sorry, your input was invalid, pick a number from 10-99")





    





  # Defending





  # Physical  


  
  
  
  