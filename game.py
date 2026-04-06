"""
game.py""" 
"""Main game file of AdventureGameProject, contains
main game loop.
"""
from gamefunctions import new_random_monster
from gamefunctions import purchase_item
from gamefunctions import print_shop_menu
from gamefunctions import print_welcome
from gamefunctions import town_menu
from gamefunctions import town_select_1
from gamefunctions import town_select_2
from gamefunctions import town_select_3
#from gamefunctions import displayFightStatistics
import random

#DEFAULT USER CHAR VARIABLES
user_char_health = 15
user_char_money = float(100.00)
user_char_power = 4

#MONSTER STATS VARIABLES
monster_name = "default"
monster_desc = "default"
monster_health = 1
monster_power = 1
monster_money = 1

#GAME RUNNING? BOOLEAN
running = True

username = input("Please enter your name:\n") #prompt user to enter name 
print(print_welcome(username, 20)) #greet user by name

#MAIN GAME LOOP
while running == True:

    town_menu()
    
    if town_select_1:
        town_menu()
    
    if town_select_2:
        town_menu()

    if town_select_3:
        town_select_3()
        
