import math
import random
list1 = list(range(10-100))
#Pace
def pace():
  print("Enter a number from 10 - 99, the higher the number the better!")
  acceleration = int(input("Acceleration: "))
  sprint_speed = int(input("Sprint Speed: "))
  pace1 = round((acceleration + sprint_speed) / 2)
  print(f"Player Pace: {pace1}")
  while acceleration not in list1:
    acceleration = int(input("Acceleration: "))
  while sprint_speed not in list1:
    sprint_speed = int(input("Sprint Speed: "))


  # Shooting
#def shooting():





  # Passing
#def passing():




  # Dribbling
dribbling_list = [] 
max_length = 6
dribbling_input = int(input("Enter your player's agility, balance, reactions, ball control, dribbling, and composure in this order."))

def dribbling_stats(dribbling_values, dribbling_list, max_length, dribbling_input):
  while True:
    dribbling input
    while len(dribbling_list) <= max_length:
      dribbling_list.append(dribbling_input)
  print(f"Your dribbling inputs: {dribbling_list} ") 


def dribbling_stat(sum):
  sum = dribbling_list(sum)
  final_dribbling = sum/2
  print(f"Your player's final dribbling stat: {final_dribbling} ")


    





  # Defending





  # Physical  


  
  
  
  