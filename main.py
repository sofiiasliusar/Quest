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
        print(f"{self.name} атакує суперника {enemy.name} на {damage} балів втрати життєвої енергії!")

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
        print(f"{self.name} атакує гравця {player.name} на {damage} балів втрати життєвої сили!")

def intro():
    print("Вітаю у грі!")
    print("Ви летите на повітряній кулі.")
    print("Ваша ціль знайти скарб.")
    print("Ви можете приземлитись на озері (1), в лісі (2), або полетіти далі в космос (3).")
    print("Ваш вибір?")

def first_choice():
    choice1 = input("1, 2, або 3? ")
    if choice1 == "1":
        underwater_world()
    elif choice1 == "2":
        magical_forest()
    elif choice1 == "3":
        outer_space
    else:
        print("Будьте серйозні, будь ласка!")
        first_choice()

def underwater_world():
    print("Ви потрапили у підводний світ. Куди хочете далі? \nЗакопатись в пісок і запитати в Сома де скарб (1), у гості до Зевса (2), на риболовлю (3)")
    choice2 = input("Що ви оберете?")
    if choice2 == "1":
        choice21 = input("За допомогою своєї блискучої інтуїції ви знайшли Сома з першого разу. Як ви його запитаєте? \nHello, how are you Som? Where is the treasure? (1) \nБуль-буль, буль буль буль. Буль? (2)")
        if choice21 == "1":
            print("Сом: I`m good. Thank you! It's right here!")
            find_treasure()
        elif choice21 == "2":
            print("Сом: Буль-буль!")
            print("Сом сприйняв це, як хамство :(")
            in_prison()
    elif choice2 == "2":
        print("Зевс вас прийняв, як дорогого гостя. Ви наїлись мушель і забули про скарб :(")
        game_lost()
    elif choice2 == "3":
        print("У цьому підводному світі риболовля - НЕЗАКОННА! \nНезнання закону не звільняє від відповідальності! \nУ вас є право зберігати мовчання! \nВсе, що ви скажете може і буде використано проти вас!")
        in_prison()
    else:
        print("Будьте серйозні, будь ласка!")
        underwater_world()

def in_prison():
    print("Ви потрапили в тюрму. Щоб вийти на свободу і повернути час назад вам потрібно перемогти Лохнеське Чудовисько, Вужика або Мокру Курку!")
    fight_escape()

def fight_escape():
    player_name = input("Виберіть собі потужний псевдонім: ")
    player = Player(player_name)

    enemies = [Enemy("Мокра Курка", 20, 5), Enemy("Лохнеське Чудовисько", 30, 8), Enemy("Вужик", 50, 15)]
    enemy = random.choice(enemies)
    print(f"З'являється серйозно налаштований суперник - {enemy.name} !\n")

    while enemy.is_alive():

        
        while enemy.is_alive() and player.is_alive():
            action = input("Що будете робити? \n Бити ногами (1), \n Не бити ногами (2)? : ")
            
            if action == "1":
                player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(player)
            elif action == "2":
                print("Ви зробили правильний вибір і зекономили собі життєву енергію.")
                break
            else:
                print("Будьте серйозні, будь ласка!")
        
        if not player.is_alive():
            print("Ви не розрахували сили і програли.")
            in_prison()
        else:
            print(f"Ви перемогли. Ваш суперник {enemy.name} - програв! Ваша життєва енергія: {player.health}\n")
            intro()

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
        print("Будьте серйозні, будь ласка!")
        encounter_monster()

def find_treasure():
    print("""  
           .--..--..--..--..--..--.
         .' \  (`._   (_)     _   |
       .'    |  '._)         (_)  |
       \ _.')\      .----..---.   /
       |(_.'  |    /    .-\-.  \  |
       \     0|    |   ( O| O) | o|
        |  _  |  .--.____.'._.-.  |
        \ (_) | o         -` .-`  |
         |    \   |`-._ _ _ _ _\ /
         \    |   |  `. |_||_|   |
         | o  |    \_      \     |     -.   .-.
         |.-.  \     `--..-'   O |     `.`-' .'
       _.'  .' |     `-.-'      /-.__   ' .-'
     .' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
     `-._  `.  |________/\_____|    `-.'
        .'   ).| '=' '='\/ '=' |
        `._.`  '---------------'
                //___\   //___/
                  ||       ||
                  ||_.-.   ||_.-.
                 (_.--__) (_.--__)
    """)
    print("Ви знайшли скарб і порвали цю гру!!!")

def game_lost():
    print("""
        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    |
   /        .-----.        |
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              | |
             _| |_
            /\( )/|
           /  ` '  |
          | |     | |
          '-'     '-'
          | |     | |
          | |     | |
          | |-----| |
       .`/  |     | |/`.
       |    |     |    |
       '._.'| .-. |'._.'
             \ | /
             | | |
             | | |
             | | |
            /| | ||
          .'_| | |_`.
          `. | | | .'
       .    /  |  \    .
      /o`.-'  / \  `-.`o|
     /o  o\ .'   `. /o  o|
     `.___.'       `.___.'
        """)

def main():
    intro()
    first_choice()

main ()