"""gamefunctions.py"""
"""AdventureGameProject module, 4 separate functions: print_welcome, print_shop_menu, purchase_item, new_random_monster.

print_welcome = function that greets the player 
with formatted and centered 
text based on inputted name.

print_shop_menu = function that outputs a formatted menu of 
items and their prices based on 
inputted items and inputted prices.

purchase_item = function that takes a player's 
current money, the number of items 
they wish to purchase, and the cost 
of each item as input
and returns the remaining balance and 
amount of items they have purchased.

new_random_monster = returns a randomly selected monster with 
randomized stats.


"""
#gamefunctions.py
#Autumn Harris
#4/4/2026

import random

#IS GAME RUNNING?
running = True

#PRINT WELCOME FUNC
def print_welcome(name, width):
    """
    Greets player by name, formats greeting to be centered.
    
    Parameters:
        name (str): Name of the player to add.
        width (int): Width of chars for greeting format.

    Returns:
        None
    
    Example:
        >>> name = input("Autumn")
        >>> width(30)
        >>> print_welcome("Autumn", 30)
                Hello, Autumn!       
    """
    print_msg = f"Hello, {name}!"
    center_print_msg = print_msg.center(width, " ")
    
    print(center_print_msg)
    return

#PRINT SHOP MENU FUNC
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """
    Prints formatted shop menu with prices for each item.
    
    Parameters:
        item1Name (str): Name of first item in shop menu.
        item1Price (float): Price of first item in shop menu.
        item2Name (str): Name of second item in shop menu.
        item2Price (float): Price of second item in shop menu.
    
    Returns:
        None

    Example:
        >>> item1Name = "Knife"
        >>> item1Price = 17.69
        >>> item2Name = "Backpack"
        >>> item2Price = 27.15
        >>> print_shop_menu("Knife", 17.69, "Backpack", 27.15)
        /----------------------\\
        | Knife          $17.69|
        | Backpack       $27.15|
        \\----------------------/
    """
    price_1 = f"${item1Price:.2f}"
    price_2 = f"${item2Price:.2f}" 

    print("/----------------------\\")
    print(f"| {item1Name:<12} {price_1:>8}|")
    print(f"| {item2Name:<12} {price_2:>8}|")
    print("\\----------------------/")
    return

#PURCHASE ITEM FUNC
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """
    Purchase items and return remaining balance
    of player's money based on starting balance,
    item cost, and number of purchased items.

    Parameters:
        itemPrice (int): Cost of each item.
        startingMoney (int): Player's starting balance.
        quantityToPurchase (int): Number of items
        player purchases, defaults to 1 without
        input.
    
    Returns:
        total_leftover_total_purchase = leftover money
        and amount of items purchased

    Example:
        >>> itemPrice = 100
        >>> startingMoney = 1000
        >>> quantityToPurchase = 5
        >>> purchase_item(100, 1000, 5)
        >>> money_transaction = purchase_item(100, 1000, 5)
        >>> print(money_transaction) 
        [500, 5]
    """
    #function variables
    max_budget = startingMoney // itemPrice
    num_purchased = min(quantityToPurchase, max_budget)
    leftover_money = startingMoney - (num_purchased * itemPrice)

    #function output list to be returned
    total_leftover_total_purchase = [leftover_money, num_purchased]
    return total_leftover_total_purchase

#IMPORT RANDOM PY MODULE
import random

#RANDOM MONSTER FUNC
def new_random_monster():
    """
    Outputs a random monster with randomized stats
    based on each monster's associated dictionary.
    
    Parameters:
        None
    
    Returns:
        random_my_monster

    Example:
        >>> my_monster = new_random_monster()
        >>> print(my_monster['name'])
        >>> print(my_monster['description'])
        >>> print(my_monster['power'])
        >>> print(my_monster['health'])
        >>> print(my_monster['money']) 
        Bandit
        An opportunistic raider, armed with scavenged, poorly-maintained weaponry.
        6
        9
        15
    """
    #monster types and stats dicts
    my_monster_bandit = {
       "name": "Bandit",
       "description": "An opportunistic raider, armed with scavenged, poorly-maintained weaponry.",
       "power": random.randint(1, 6),
       "health": random.randint(2, 9),
       "money": random.randint(3, 25)
    }

    my_monster_mutant = {
        "name": "Mutant",
        "description": "A lone, sickly figure. They are deformed by constant exposure to pollution. Their eyes look sad.",
        "power": random.randint(1, 3),
        "health": random.randint(1, 5),
        "money": random.randint(2, 7)
    }

    my_monster_packdogs = {
        "name": "Pack of dogs",
        "description": "A pack of wild dogs. Comprised of many breeds. Before the Fall these were pets, but now they look gaunt and ravenous.",
        "power": random.randint(3, 8),
        "health": random.randint(3, 15),
        "money": random.randint(1, 3)
    }

    #randomize monster selection
    my_monster_tuple = (my_monster_bandit, my_monster_mutant, my_monster_packdogs)
    random_my_monster = random.choice(my_monster_tuple)
    

    return random_my_monster



#USER CHAR STATS VARIABLES
user_char_health = 15
user_char_money = float(100.00)
user_char_power = 4

#MONSTER STATS VARIABLES
monster_name = "default"
monster_desc = "default"
monster_health = 1
monster_power = 1
monster_money = 1

def town_select_1(): #SELECT 1 = monsterFUNCT
    """
    When function is run Player fights 1 of 3 randomly
    selected monsters and allows Player to fight
    or flee based on input.
    Parameter: None
    Returns: None
    """

    print("You gather your items, strolling past the guarded gates you leave the shantytown.")
    print("Looking at the bleak, desolate landscape ahead of you, your muscles tense.")
    print("You ready your weapon. You can sense danger nearby.")

    global user_char_health
    global user_char_money
    global user_char_power

    global monster_name
    global monster_desc
    global monster_health
    global monster_power
    global monster_money

    random_monster = new_random_monster()

    monster_name = random_monster['name']
    monster_desc = random_monster['description']
    monster_health = random_monster['health']
    monster_power = random_monster['power']
    monster_money = random_monster['money']

    def displayFightStatistics():
        """
        Displays monster and player health and power throughout fight.
        Parameters: None
        Returns: None
        """

        print(f"Player\nHealth: {user_char_health}\nAttack: {user_char_power}")
        print(f"{monster_name}\nHealth: {monster_health}\nAttack: {monster_power}")

    
    
    print(monster_name)
    print(monster_desc)

    print(f"{monster_name} attacks for {monster_power} points of damage!")
    print(f"Player attacks {monster_name} for {user_char_power} points of damage!")
    
    
    monster_health = monster_health - user_char_power
    user_char_health = user_char_health - monster_power
    
    displayFightStatistics()

    while user_char_health > 0 and monster_health > 0:
        user_action = input("Select:\n1. Fight\n2. Flee\n")
        
        #getUserFightAction(user_char_stats, monster_stats)

        if user_action == "1":
            monster_health = monster_health - user_char_power
            user_char_health = user_char_health - monster_power
            displayFightStatistics()

        elif user_action == "2":
            print("You ran away")
            break # exits the while loop

        else:
            print("Invalid selection!") # prints an error but stays in the loop

    # Handle the cases that cause the loop to end
    if user_char_health <= 0:
        print("Your character passed out")
    
    else:
        user_char_money = user_char_money + monster_money
        
    return

def town_select_2(): #SELECT 2 = restFUNCT
    """
    When function runs takes $5 of Player money
    and restores 3 Player health.
    Parameters: None
    Returns: None
    """
    print("You enter the hostel. The smell of body odor, machine oil, and cigarettes is overwhelming.") 
    print("You pay $5 and find a quiet corner of straw and blankets to hunker down.")
    print("Your eyelids are heavy and seem to close on their own.")
    print("You rest for the night, your body stiff and aching.")
    global user_char_health
    global user_char_money

    user_char_health = user_char_health + int(3)
    user_char_money = user_char_money - float(5.00)

    return

def town_select_3(): #SELECT 3 = quitFUNCT
    """
    Prints quit of main game loop.
    
    Parameters: None
    Returns: None
    """
    print("Quitting program...")
    print(f"Goodbye!")

    global running
    running = False
    quitgame = running

    return quitgame


def town_menu(): #Town menu function
    """
    Main game menu, allows player input to select run
    functions
    Parameters: None
    Returns: None
    
    """
    print("You are in town.")
    print(f"Current health: {user_char_health}, Current money: ${user_char_money:.2f}")
    print("What would you like to do?\n")
    print("1) Leave town (Fight Monster)\n2) Sleep (Restore HP for $5)\n3) Quit")
    
    town_select = int(input())
    if town_select == 1:
        town_select_1()
    elif town_select == 2:
        town_select_2()
    elif town_select == 3:
        town_select_3()
    else:
        print("That is not a valid selection!")

    return

#if __name__ == "__main__":



