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
        outer_space()
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
        print_with_pause("Ви зайшли до затишного кафе. Який же тут запах!")
        in_cafe()
    elif choice3 == "3":
        hello_kitty()
    else:
        print_with_pause("Будьте серйозні, будь ласка!")
        magical_forest()

def witch_house():
    print_with_pause("Хатинка відьми - це найкраще місце для вирішення проблем!")
    print_with_pause("Але все не так просто!")
    print_with_pause("Її хатинку охороняє той самий 'злий пес'!")
    fight_dog()
    
def fight_dog():
    print_with_pause("Щоб пройти, потрібно прориватись!")
    print_with_pause("Оцініть риски! ___ ___ ___")
    print_with_pause("Хочете втекти (1) чи прорватись (2)?")
    action = input("?")
    if action == "1":
        print_with_pause("Ви ще і не заходили.")
        print_with_pause("Тому можете вважати, що ви втекли.")
        print_with_pause("Але вам треба всередину.")
        fight_dog()
    elif action == "2":
        if random.randint(0, 1) == 1:
            print_with_pause("Вітаю! Ви прорвались!")
            hello_witch()
        else:
            print_with_pause("Ви ПОРвались на кусочки.")
            print_with_pause("...")
            print_with_pause("Не забувайте! Ви в чарівному лісі!")
            print_with_pause("Загадайти подумки бажання стати трансформером і зібратись докупи.")
            print_with_pause("І воно обов'язково збудеться!")
            print_with_pause("...")
            print_with_pause("...")
            print_with_pause("...")
            print_with_pause("У вас вийшло!")
            fight_dog()
    else:
        print("Будьте серйозні, будь ласка!")
        fight_dog()

def hello_witch():
    print_with_pause("...")
    print_with_pause("...Злий сміх...")
    print_with_pause("Відьма: Хочеш вирішення проблем?")
    print_with_pause("Обирай зілля!")
    print_with_pause("1: Оранжеве зілля зробить тебе БОГАЧЕМ :D")
    print_with_pause("2: Фіолетове подарує зустріч з Анджеліною Джолі!")
    print_with_pause("3: Веселкове - все і одразу! :D")
    choice8 = input("?")
    if choice8 == "1":
        print_with_pause("Відьма: Все, як обіцяла!")
        find_treasure()
    elif choice8 == "2":
        print_with_pause("Відьма: Все, як обіцяла!")
        a_j()
    elif choice8 == "3":
        print_with_pause("...Злий сміх...")
        print_with_pause("Відьма: 'Все і зразу' не буває :D")
        print_with_pause("Відьма: Хто хоче все і зразу, отримує нічого і поступово :D")
        game_lost()        
    else: 
        print("Будьте серйозні, будь ласка!")
        hello_witch()

def in_cafe():
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
    print_with_pause("засмагати (2)")
    print_with_pause("бігати за метеликами (3)")

    choice5 = input("?")
    if choice5 == "1":
        play_football()
    elif choice5 == "2":
        sun_bathe()
    elif choice5 == "3":
        hello_butterfly()
    else:
        print_with_pause("Щось ви замріялись!")
        in_dream()

def play_football():

    print_with_pause("Гра Португалія - Україна.")
    print_with_pause("Після надзвичайно напруженої гри додали 5 хвилин додаткового часу.")
    print_with_pause("Вибуло по 10 гравців з кожної команди.")
    print_with_pause("Залишились тільки ви і Роналду.")
    print_with_pause("...")
    print_with_pause("Небезпечний момент!!!")
    print_with_pause("...")
    print_with_pause("Роналду випадково зіграв рукою.")
    print_with_pause("...")
    shoot_penalty()
    
def shoot_penalty():
    print_with_pause("Суддя назначає пенальті.")
    print_with_pause("...")
    print_with_pause("Ви б'єте пенальті!")
    print_with_pause("Куди будете бити?") 
    print_with_pause("вліво (1)")
    print_with_pause("в центр (2)")
    print_with_pause("вправо (3)")
    player_choosing = input("?")
    if player_choosing == "1":
        player_choice = "вліво"
    elif player_choosing == "2":
        player_choice = "в центр"
    elif player_choosing == "3":
        player_choice = "вправо"
    else:
        print_with_pause("Будьмо уважні!")
        shoot_penalty()

    goalkeeper_choice = random.choice(["вліво", "в центр", "вправо"])

    print(f"Ви б'єте {player_choice}, і Роналду робить стрибок {goalkeeper_choice}.")
    
    if player_choice == goalkeeper_choice:
        print("Роналду зловив!")
        main_game()
    else:
        print("ГООООООООООЛ!!!")
        your_victory()
                    
def main_game():
    # player_score = 0
    # ronaldo_score = 0
    # if shoot_penalty():
    #     ronaldo_score += 1
    # else:
    #     player_score += 1
    
        # while player_score <= ronaldo_score:
    # if player_score > ronaldo_score:
    #     print_with_pause("Гру закінчено з рахунком:")
    #     print_with_pause(f"Україна {player_score} - {ronaldo_score} Португалія")
    # else:
            # print(f"Рахунок: Україна {player_score} - {ronaldo_score} Португалія")

            # if player_choice == goalkeeper_choice:
            #     ronaldo_score += 1
            # else:
            #     player_score += 1
 
        # if shoot_penalty():
        #     ronaldo_score += 1
        # else:
        #     player_score += 1
            
        # print(f"Рахунок: Україна {player_score} - {ronaldo_score} Португалія")
    print_with_pause("Ви побачили, що Роналду знову зіграв рукою.")
    print_with_pause("Скажете судді?")
    play_again = input("Так (1), Ні (2)?")
    if play_again == "1":
        shoot_penalty()
    else: 
        print_with_pause("Ви посумнівались трохи, а потім вирішили сказати.")
        shoot_penalty()
    
def your_victory():
    print_with_pause("Ну ви даєте! Ви перемогли!!!")
    print_with_pause("А також...")
    print_with_pause("Ви виграли пожиттєвий запас шампуню від Роналду. Це справжній скарб!!!")
    find_treasure()

def sun_bathe():
    print_with_pause("Ви почали засмагати :)")
    print_with_pause("Сонечко так гарно гріє :)")
    print_with_pause("...")
    print_with_pause("Ви розслабляєтесь :)")
    print_with_pause("...")
    print_with_pause("Ви перегрілись і очманіли.")
    print_with_pause("Це вже подвійне очманіння!?!")
    print_with_pause("Спершу - чай, а тепер - сонце !?!")
    print_with_pause("Ви прокидаєтесь...")
    print_with_pause("І переноситесь назад в кафе.")
    in_cafe()
       
def hello_butterfly():
    print_with_pause("Ви бігаєте по м'ягенькій травичці :)")
    print_with_pause("Ваш розум вільний від думок :)")
    print_with_pause("Ваша душа спокійна :)")
    print_with_pause("Який чудовий день!")
    print_with_pause("Яке свіже повітря!")
    print_with_pause("Які гарні метелики літають поруч!")
    print_with_pause("Що це за звук?")
    print_with_pause("Звучить, як дзвіночок!")
    print_with_pause("А ні! Це ж метелик з вами привітався!")
    print_with_pause("Раптом... Ви помічаєте море кольорових метеликів довкола! :D")
    print_with_pause("На якому ви хочете полетіти?")
    print_with_pause("На синьому (1)")
    print_with_pause("На червоному (2)")
    print_with_pause("На сіро-буро-малиновому (3)")
    choice6 = input("?")
    if choice6 == "1":
        blue_butterfly()
    elif choice6 == "2":
        red_butterfly()
    elif choice6 == "3":
        sbm_butterfly()

def blue_butterfly():
    print_with_pause("Ви підійшли до синього метелика і питаєте:")
    print_with_pause("Ви: Метелику-метелику! А ти знаєш де скарб?")
    print_with_pause("Метелик: Ні, на жаль, не знаю. Але я синій метелик і можу віднести тебе в синє місце!")
    print_with_pause("Вам сподобалась ця ідея і ви погодились.")
    print_with_pause("Вжуууух!")
    print_with_pause("...")
    underwater_world()

def red_butterfly():
    print_with_pause("Ви підійшли до червоного метелика і питаєте:")
    print_with_pause("Ви: Метелику-метелику! А ти знаєш де скарб?")
    print_with_pause("Метелик: Так, знаю. Я тебе туди віднести!")
    print_with_pause("Вжуууух!")
    print_with_pause("...")
    print_with_pause("Ви полетіли високо-високо до неба.")
    print_with_pause("Аааааж до хмар.")
    print_with_pause("Хмари стали густіші...")
    print_with_pause("Більше схожі на дим...")
    print_with_pause("...")
    print_with_pause("Це і є дим.")
    print_with_pause("Ви з метеликом вилітаєте з димаря кафе, що в чарівному лісі...")
    print_with_pause("Летите на північ...")
    print_with_pause("Через дикий холод і лютий мороз...")
    print_with_pause("Ви звертаєте, робите мертву петлю...")
    print_with_pause("...")
    print_with_pause("Тепер ви прямуєте до величезного активного вулкана!!! :О")
    print_with_pause("Червоний метелик не хоче попекти крила і ви прощаєтесь!")
    print_with_pause("...")
    print_with_pause("Далі ви пересуваєтесь, як лицар на білому коні!")
    print_with_pause("Ви скачете через гострі, високі скелі...")
    print_with_pause("...перескакуєте через вогонь...")
    print_with_pause("Добираєтесь до жерла вулкана.")
    print_with_pause("Ви винаходите підводний корабель, щоб спуститись в лаву.")
    print_with_pause("На дні вулкана знаходите омріяний скарб!!!")
    print_with_pause("Вітаю!!!")
    find_treasure()    

def sbm_butterfly():
    print_with_pause("Ви підійшли до сіро-буро-малинового метелика і питаєте:")
    print_with_pause("Ви: Метелику-метелику! А ти знаєш де скарб?")
    print_with_pause("Метелик: Так, знаю. Мені по дорозі.")
    print_with_pause("Метелик: Я візьму тебе з собою.")
    print_with_pause("...")
    print_with_pause("Метелик: ЯКЩО...")
    print_with_pause("...")
    print_with_pause("Метелик: Ти відгадаєш загадку!")
    print_with_pause("Ви, як азартна людина, погодились.")
    solve_puzzle()
def solve_puzzle():
    print_with_pause("Метелик: Сів метелик на травичку і сказав якусь ... ?")
    print_with_pause("1: Небеличку")
    print_with_pause("2: Суничку")
    print_with_pause("3: Дурничку")
    choice7 = input("?")
    if choice7 == "1":
        solve_puzzle()
    elif choice7 == "2":
        solve_puzzle()
    elif choice7 == "3":
        correct_answer()
def correct_answer():
    print_with_pause("Метелик: Правильно! Полетіли!")
    print_with_pause("Вжуууух!")
    find_treasure()

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
    print_with_pause("Ви вийшли з орбіти Землі.")
    print_with_pause("Вам пощастило, що ви були в скафандрі.")
    print_with_pause("А то би програли...")
    print_with_pause("У космосі холодно.")
    print_with_pause("Але в скафандрі тепло :)")
    print_with_pause("Перед вами космічне роздоріжжя:")
    print_with_pause("1: Марс")
    print_with_pause("2: Нептун")
    print_with_pause("3: Сатурн")
    choice9 = input("На яку хочете планету?")
    if choice9 == "1":
        mars_planet()
    elif choice9 == "2":
        neptun_planet()
    elif choice9 == "3":
        saturn_planet()       
    else: 
        print("Будьте серйозні, будь ласка!")
        outer_space()

def mars_planet():
    print_with_pause("На марсі ви зустріли...")
    print_with_pause("Кого?")
    print_with_pause("...")
    print_with_pause("Ну кого?")
    print_with_pause("Правильно! Марсіанина!")
    print_with_pause("Він вас кличе в Голлівуд :D")
    print_with_pause("...і хоче познайомити з:")
    print_with_pause("1:Джонні Деппом")
    print_with_pause("2:Бредом Пітом")
    print_with_pause("3:Анджеліною Джолі")
    choice10 = input("?")
    if choice10 == "1":
        j_d()
    elif choice10 == "2":
        b_p()
    elif choice10 == "3":
        a_j()       
    else: 
        print("Будьте серйозні, будь ласка! Це космос!")
        outer_space()

def j_d():
    print_with_pause("Джонні Депп в ролі шапочника: Улюблене число кролика - 7.")
    print_with_pause("Джонні Депп в ролі шапочника: Іди в ліс і шукай кролячу яму!")
    magical_forest()

def b_p():
    print_with_pause("Ви з Бредом Пітом тепер коріша.")
    print_with_pause("Ви разом ідете в перукарню!")
    print_with_pause("Вам не пощатило зі стрижкою D:")
    print_with_pause("Ви завстидались виходити і не змогли продовжити пошуки скарбу D:")
    game_lost()

def a_j():
    print_with_pause("Ви зустрілись з неймовірною Анджеліною Джолі!")
    print_with_pause("Вона передала для України мільйон доларів!")
    find_treasure()

def neptun_planet():
    print_with_pause("Виявляється на Нептуні є великий океан!")
    print_with_pause("Там живе Нептун.")
    print_with_pause("Він запрошує вас в гості...")
    print_with_pause("...і пригощає космічно-морськими смаколиками.")
    print_with_pause("Він ділиться цінною порадою.")
    print_with_pause("Нептун: Не їж ракушки в Зевса.")
    print_with_pause("А ще показує тобі свій космічно-морський замок :D")
    print_with_pause("Нептун: А це - мій портал до морського світу Землі!")
    print_with_pause("...")
    underwater_world()

def saturn_planet():
    print_with_pause("Хоч Сатурн і схожий на веселу планету з колечками...")
    print_with_pause("Насправді, тут все серйозно.")
    print_with_pause("Хочеш скарб - забери в космічного монстра!")
    print_with_pause("...")
    fight_dragon()

def fight_dragon():
    player_name = input("Виберіть собі потужний псевдонім: ")
    player = Player(player_name)

    enemies = [Enemy("Вуса Зіброва", 20, 5), Enemy("Бабайко", 30, 8), Enemy("Капітан Очевидність", 50, 15)]
    enemy = random.choice(enemies)
    print_with_pause(f"З'являється серйозно налаштований суперник - {enemy.name} !\n")

    while enemy.is_alive():

        
        while enemy.is_alive() and player.is_alive():
            action = input("Що будете робити? \n Стріляти лазерами (1), \n Не стріляти лазерами (2)? : ")
            
            if action == "1":
                player.attack_enemy(enemy)
                if enemy.is_alive():
                    enemy.attack_player(player)
            elif action == "2":
                print_with_pause("Ви зробили правильний вибір і зекономили собі заряд скафандра.")
                break
            else:
                print_with_pause("Будьте серйозні, будь ласка!")
        
        if not player.is_alive():
            print_with_pause("Ви не розрахували сили і програли.")
            saturn_planet()
        elif not enemy.is_alive():
            print_with_pause(f"Ви перемогли. Ваш суперник {enemy.name} - програв! Ваш заряд скафандра: {player.health}\n")
            print_with_pause("Ви забираєте в монстра скарб! Вітаю!")
            print_with_pause("...")
            find_treasure()
        else:
            print_with_pause("Продовжуйте бій. Ризикуйте і йдіть в атаку!")

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
