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
randomized stats."""

#gamefunctions.py
#Autumn Harris
#3/24/2026

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

#TEST FUNCTIONS

if __name__ == "__main__":
    print(new_random_monster())

    print(purchase_item(100, 1000, 5))

    print(print_shop_menu("Knife", 17.69, "Backpack", 27.15))

    print(print_welcome("Autumn", 30))
    

