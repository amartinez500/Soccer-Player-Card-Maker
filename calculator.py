import math
import random
my_list = list(range(10,100,1)) 

#Pace
def pace(my_list):
  print("Enter a number from 10 - 99, the higher the number the better!")
  acceleration = int(input("Acceleration: "))
  sprint_speed = int(input("Sprint Speed: "))
  pace1 = round((acceleration + sprint_speed) / 2)
  print(f"Player Pace: {pace1}")
  # while acceleration not in list1:
  #   acceleration = int(input("Acceleration: "))
  # while sprint_speed not in list1:
  #   sprint_speed = int(input("Sprint Speed: "))


  # Shooting
#def shooting():





  # Passing
#def passing():




  # Dribbling
dribbling_list = [] 
max_length = 6

def dribbling_stats(dribbling_list, max_length, sum):
  while True:
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


  
  
  
  