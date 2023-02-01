import math
import random

#asking for name a positioning og the player
def name_position():
  list2 = ["LB","RB","CB","LWB","RWB","CDM","CM","CAM","LM","RM","LW","RW","CF","ST"]
  print("Fifa 23 Card Creator")
  player = input("What is the players name?").lower()
  print("LB,RB,CB,LWB,RWB,CDM,CM,CAM,LM,RM,LW,RW,CF,ST")
  position = input("What position do want him to be? The positions are listed above↑").lower()


list1=list(range(10,100))
#def pace1():
  #return pace(list1)
#pace
def pace(list1):
  print("Enter a number from 10 - 99, the higher the number the better!")
  acceleration = int(input("Acceleration: "))
  sprint_speed = int(input("Sprint Speed: "))
  pace1 = round((acceleration + sprint_speed) / 2)
  #print(f"Your player's pace: {pace1} ")
  if acceleration and sprint_speed not in list1:
    print("Sorry pick a number from 10-99!")
    return pace(list1)
  else:
   print(f"Your player's pace: {pace1} ")


  # Shooting
#def shooting():





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


  
  
  
  