from gamefunctions import new_random_monster
from gamefunctions import purchase_item
from gamefunctions import print_shop_menu
from gamefunctions import print_welcome

#prompt user to enter name, greet user by name
username = input("Please enter your name:\n")
print(print_welcome(username, 30))

print(new_random_monster())

print(purchase_item(100, 1000, 5))

print(print_shop_menu("Knife", 17.69, "Backpack", 27.15))

