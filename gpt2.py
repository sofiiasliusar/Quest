import random

def introduction():
    print("Welcome to the Quest Game!")
    print("You find yourself in a mysterious forest.")
    print("Your goal is to find the hidden treasure.")
    print("You can go left or right.")
    print("Choose your path carefully!")

def choose_path():
    choice = input("Do you want to go left or right? ").lower()
    if choice == "left":
        encounter_monster()
    elif choice == "right":
        find_treasure()
    else:
        print("Invalid choice. Try again.")
        choose_path()

def encounter_monster():
    print("Oh no! You've encountered a fearsome monster!")
    action = input("Do you want to fight or run? ").lower()
    if action == "fight":
        if random.randint(0, 1):
            print("Congratulations! You defeated the monster and found the treasure!")
        else:
            print("You were defeated by the monster. Game over.")
    elif action == "run":
        print("You managed to escape from the monster.")
        choose_path()
    else:
        print("Invalid choice. Try again.")
        encounter_monster()

def find_treasure():
    print("You've found the hidden treasure!")
    print("Congratulations, you win!")

def main():
    introduction()
    choose_path()



introduction()
choose_path()
encounter_monster()
find_treasure()