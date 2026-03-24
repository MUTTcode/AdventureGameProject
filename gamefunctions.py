#gamefunctions.py
#Autumn Harris
#3/24/2026

#GAME FUNCTIONS: PRINT WELCOME AND PRINT SHOP MENU

#PRINT WELCOME FUNC
def print_welcome(name, width):
    """This function greets the player by name and centers the greeting based on the width value"""
    print_msg = f"Hello, {name}!"
    center_print_msg = print_msg.center(width, " ")
    
    print(center_print_msg)

#PRINT WELCOME FUNC OUTPUT 3 TIMES
print_welcome("Autumn", 30)
print_welcome("Brace", 20)
print_welcome("Briar", 40)

#PRINT SHOP MENU FUNC
def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """This function prints out a formatted shop menu with prices included for each item"""
    price_1 = f"${item1Price:.2f}"
    price_2 = f"${item2Price:.2f}" 

    print("/----------------------\\")
    print(f"| {item1Name:<12} {price_1:>8}|")
    print(f"| {item2Name:<12} {price_2:>8}|")
    print("\\----------------------/")

#PRINT SHOP MENU FUNC OUTPUT 3 TIMES
print_shop_menu("Chicken", 5.00, "Bread", 7.00)
print_shop_menu("Cheese", 3.54, "Ammo", 22.40)
print_shop_menu("Knife", 17.69, "Backpack", 27.15)




#GAME FUNCTIONS: PURCHASE ITEMS AND RANDOM MONSTERS

#PURCHASE ITEM FUNC
def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """This function considers the amount of money a player starts with, amount of items to purchase, and item cost"""
    """This function returns the amount of remaining money a player has after purchasing a selected number of items"""
    #function variables
    max_budget = startingMoney // itemPrice
    num_purchased = min(quantityToPurchase, max_budget)
    leftover_money = startingMoney - (num_purchased * itemPrice)

    #function output list to be returned
    total_leftover_total_purchase = [leftover_money, num_purchased]

    return total_leftover_total_purchase

#OUTPUT OF PURCHASE ITEM FUNC 3 TIMES

#print money transaction 1
money_transaction = purchase_item(400, 1000)
print(money_transaction)

#print money transaction 2
money_transaction = purchase_item(10, 100, 11)
print(money_transaction)

#print money transaction 3
money_transaction = purchase_item(100, 1000, 5)
print(money_transaction)

#import random py module
import random

#RANDOM MONSTER FUNC
def new_random_monster():
    """This function outputs a random monster with randomized stats selected from a range of values"""
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

#OUTPUT OF RANDOM MONSTERS FUNC 3 TIMES
#print random monster 1
my_monster = new_random_monster()
print(my_monster['name'])
print(my_monster['description'])
print(my_monster['power'])
print(my_monster['health'])
print(my_monster['money'])

#print random monster 2
my_monster = new_random_monster()
print(my_monster['name'])
print(my_monster['description'])
print(my_monster['power'])
print(my_monster['health'])
print(my_monster['money'])

#print random monster 3
my_monster = new_random_monster()
print(my_monster['name'])
print(my_monster['description'])
print(my_monster['power'])
print(my_monster['health'])
print(my_monster['money'])