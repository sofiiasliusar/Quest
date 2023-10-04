import random
import time

def print_with_pause(text):
    print(text)
    time.sleep(1)

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
    print_with_pause("Вітаю у грі!")
    print_with_pause("Ви летите на повітряній кулі.")
    print_with_pause("Ваша ціль знайти скарб.")
    print_with_pause("Ви можете приземлитись")
    print_with_pause("на озері (1),")
    print_with_pause("в лісі (2),")
    print_with_pause("або полетіти далі в космос (3).")
    print_with_pause("Ваш вибір?")

def first_choice():
    choice1 = input("1, 2, або 3? ")
    if choice1 == "1":
        underwater_world()
    elif choice1 == "2":
        magical_forest()
    elif choice1 == "3":
        outer_space
    else:
        print_with_pause("Будьте серйозні, будь ласка!")
        first_choice()

def underwater_world():
    print_with_pause("Ви потрапили у підводний світ. Куди хочете далі?")
    print_with_pause("Закопатись в пісок і запитати в Сома де скарб (1), у гості до Зевса (2), на риболовлю (3)")
    choice2 = input("Що ви оберете?")
    if choice2 == "1":
        print_with_pause("За допомогою своєї блискучої інтуїції ви знайшли Сома з першого разу.")
        choice21 = input("Як ви його запитаєте? \nHello, how are you Som? Where is the treasure? (1) \nБуль-буль, буль буль буль. Буль? (2)")
        if choice21 == "1":
            print_with_pause("Сом: I`m good. Thank you! It's right here!")
            find_treasure()
        elif choice21 == "2":
            print_with_pause("Сом: Буль-буль!")
            print_with_pause("Сом сприйняв це, як хамство :(")
            in_prison()
    elif choice2 == "2":
        print_with_pause("Зевс вас прийняв, як дорогого гостя. Ви наїлись мушель і забули про скарб :(")
        game_lost()
    elif choice2 == "3":
        print_with_pause("У цьому підводному світі риболовля - НЕЗАКОННА!")
        print_with_pause("Незнання закону не звільняє від відповідальності!")
        print_with_pause("У вас є право зберігати мовчання! ")
        print_with_pause("Все, що ви скажете може і буде використано проти вас!")
        in_prison()
    else:
        print_with_pause("Будьте серйозні, будь ласка!")
        underwater_world()

def in_prison():
    print_with_pause("Ви потрапили в тюрму. Щоб вийти на свободу і повернути час назад вам потрібно перемогти Лохнеське Чудовисько, Вужика або Мокру Курку!")
    fight_escape()

def fight_escape():
    player_name = input("Виберіть собі потужний псевдонім: ")
    player = Player(player_name)

    enemies = [Enemy("Мокра Курка", 20, 5), Enemy("Лохнеське Чудовисько", 30, 8), Enemy("Вужик", 50, 15)]
    enemy = random.choice(enemies)
    print_with_pause(f"З'являється серйозно налаштований суперник - {enemy.name} !\n")

    while enemy.is_alive():

        
        while enemy.is_alive() and player.is_alive():
            action = input("Що будете робити? \n Бити ногами (1), \n Не бити ногами (2)? : ")
            
            if action == "1":
                player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(player)
            elif action == "2":
                print_with_pause("Ви зробили правильний вибір і зекономили собі життєву енергію.")
                break
            else:
                print_with_pause("Будьте серйозні, будь ласка!")
        
        if not player.is_alive():
            print_with_pause("Ви не розрахували сили і програли.")
            in_prison()
        elif not enemy.is_alive():
            print_with_pause(f"Ви перемогли. Ваш суперник {enemy.name} - програв! Ваша життєва енергія: {player.health}\n")
            print_with_pause("Вам вдалось повернути час назад.")
            print_with_pause("...")
            main()
        else:
            print_with_pause("Продовжуйте бій. Ризикуйте і йдіть в атаку!")

def magical_forest():
    print_with_pause("Ви опинились в чарівному лісі.")
    print_with_pause("Тут ви можете знайти вирішення своїх проблем.")
    print_with_pause("Перед вами три дороги:")
    print_with_pause("до хатинки відьми (1),")
    print_with_pause("до кафе (2),")
    print_with_pause("або до всезнаючого Чиширського кота (3)")

    choice3 = input("Куди підете?")
    if choice3 == "1":
        witch_house()
    elif choice3 == "2":
        in_cafe()
    elif choice3 == "3":
        hello_kitty()
    else:
        print_with_pause("Будьте серйозні, будь ласка!")
        magical_forest()

def witch_house():
    print_with_pause
def in_cafe():
    print_with_pause("Ви зайшли до затишного кафе. Який же тут запах!")
    print_with_pause("На вітрині ви бачите:")
    print_with_pause("Круасан (1)")
    print_with_pause("Зелений кекс (2)")
    print_with_pause("Ромашковий чай (3)")
    choice4 = input("Що ви скуштуєте?")
    if choice4 == "1":
        print_with_pause("Дуже смачно! Це справжній скарб!")
        find_treasure()
    elif choice4 == "2":
        print_with_pause("Ну ви що?")
        print_with_pause("...")
        print_with_pause("Хіба ви не знаєте?")
        print_with_pause("...")
        print_with_pause("Якщо їда викликає підозри, потрібно її викинути!!!")
        print_with_pause("Вас знудило і ви не змогли продовжити пошуки скарбу :(")
        game_lost()
    elif choice4 == "3":
        print_with_pause("Дуже ароматний і заспокійливий чай!")
        print_with_pause("Ви розслабляєтесь...")
        print_with_pause("І поринаєте в сон?...") 
        print_with_pause("Чи це інший вимір?...") 
        print_with_pause("...")
        in_dream()
    else:
        print_with_pause("Будьмо уважні!")
        in_cafe()

def in_dream():
    print_with_pause("Ви летите... \n...")
    print_with_pause("і не відчуваєте свого тіла...")
    print_with_pause("Це ніби кольоровий тунель...")
    print_with_pause("...")
    print_with_pause("...")
    print_with_pause("...")
    print_with_pause("Де ви опинитесь?..")
    print_with_pause("...")
    print_with_pause("І коли прокинитесь?")
    print_with_pause("...")
    
    print_with_pause("....Лунає голос.....")
    print_with_pause("Стюардеса: Дякуємо, що обрали наші авіалінії!")
    print_with_pause("Стюардеса: Сподіваємось, що вам сподобається подорож!")

    print_with_pause("Ви опинились на зеленій поляні з травою.")
    print_with_pause("Тільки трава і небо,")
    print_with_pause("і більше нічого...")
    print_with_pause("...")
    print_with_pause("Що будете робити?")
    print_with_pause("грати у футбол (1)")
    print_with_pause("загаряти (2)")
    print_with_pause("бігати за метеликами (3)")

    choice5 = input("?")
    if choice5 == "1":
        print_with_pause("")
        play_football()
    elif choice5 == "2":
        print_with_pause("")
        sun_bathe()
    elif choice5 == "3":
        print_with_pause("")
        hello_butterfly()
    else:
        print_with_pause("Щось ви замріялись!")
        in_dream()

def play_football():
    print

def sun_bathe():
    print

def hello_butterfly():
    print

def hello_kitty():
    print_with_pause("Здається, Кіт мав бути десь тут... ")
    print_with_pause("...")
    print_with_pause("Можливо він кудись пішов..?")
    print_with_pause("...")
    print_with_pause("А ні! От і він!")
    print_with_pause("...")
    fortunes = [
    "Якщо пес гавкає, то це просто пес, який собі просто гавкає. Це нічого не означає.",
    "Ти суслика бачиш? А він там єєєєє!",
    "Серйозне ставлення до будь-чого є фатальною помилкою.",
    "Всі найкращі люди - ненормальні, і ти в тому числі.",
    "Якщо не знаєш куди йти, то йди куди-небудь. Головне - продовжуй йти.",
    "Починай діяти, коли почуєш дзвіночок!",
    "Зроби перший крок і тоді все поступово стане на свої місця!",
    ]
    def get_random_fortune():
        return random.choice(fortunes)
    while True:
        input("Чеширський кіт: Добрррий день! Якщо вас щось цікавить, запитуйте! Я знаю абсолютно все!")
        fortune = get_random_fortune()
        print_with_pause("Чеширський кіт: ")
        print_with_pause(fortune)
    
        play_again = input("\nХочеш спробувати знову? \nТак (1) \nНі (2) \n")
        if play_again != "1":
            print_with_pause("Приходь знову!")
            print_with_pause("...")
            rabbit_hole()
            break

# def encounter_monster():
#     print("Oh no! You've encountered a fearsome monster!")
#     action = input("Do you want to fight or run? ").lower()
#     if action == "fight":
#         if random.randint(0, 1):
#             print("Congratulations! You defeated the monster and found the treasure!")
#         else:
#             print("You were defeated by the monster. Game over.")
#     elif action == "run":
#         print("You managed to escape from the monster.")
#         choose_path()
#     else:
#         print("Будьте серйозні, будь ласка!")
#         encounter_monster()
def rabbit_hole():
    print_with_pause("Ідучи від Чеширського Кота, ви впали в кролячу яму :(")
    number = input("Вгадайте число! Від 1 до 10: ")
    if number == "7":
        print_with_pause("Правильно! Вітаю!")
        find_treasure()
    else:
        print_with_pause("Неправильно! ")
        print_with_pause("Кроляча лапка вам не принесла везіння.")
        print_with_pause("Ви зламали ногу і не змогли продовжити пошуки скарбу :(")
        game_lost()

def outer_space():
    print_with_pause

def try_again():
        again = input("Так (1), Ні (2) ?")
        if again == "1":
            print_with_pause("Гаразд!")
            main()
        elif again == "2":
            print_with_pause("Нє, то нє... :)")
        else:
            print_with_pause("Будьмо уважні!")
            try_again()

def find_treasure():
    print_with_pause("""  
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
    print_with_pause("Ви знайшли скарб і порвали цю гру!!!")
    print_with_pause("...")
    print_with_pause("Хочете спробувати піти іншим шляхом? :D")
    try_again()

def game_lost():
    print_with_pause("""
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
    print_with_pause("Ви програли!")
    print_with_pause("...")
    print_with_pause("Хочете спробувати ще разочечок? :D")
    try_again()
    
   


def main():
    intro()
    first_choice()

main ()
