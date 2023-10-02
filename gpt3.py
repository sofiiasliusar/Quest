import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} for {damage} damage!")

def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    enemies = [Enemy("Goblin", 20, 5), Enemy("Orc", 30, 8), Enemy("Dragon", 50, 15)]

    while player.is_alive():
        enemy = random.choice(enemies)
        print(f"A wild {enemy.name} appears!\n")
        
        while enemy.is_alive() and player.is_alive():
            action = input("What will you do? (attack/run): ").lower()
            
            if action == "attack":
                player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(player)
            elif action == "run":
                print("You managed to escape from the battle.")
                break
            else:
                print("Invalid command. Try again.")
        
        if not player.is_alive():
            print("Game Over. You were defeated.")
        else:
            print(f"You defeated the {enemy.name}! Your health: {player.health}\n")

    print("Thanks for playing!")

main()