import random

class Player:
    def init(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.gold = 50

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name} атакує {enemy} і завдає {damage} шкоди.")
        return damage

    def show_status(self):
        print(f"{self.name}: Здоров'я: {self.health}, Золото: {self.gold}")

class Enemy:
    def init(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        print(f"{self.name} атакує {player.name} і завдає {damage} шкоди.")
        return damage

class Shop:
    def init(self):
        self.items = {"Міцний меч": 20, "Магічний пояс": 30, "Зілля лікування": 40}
        self.player_items = {}

    def show_items(self):
        print("\nМагазин:")
        for item, price in self.items.items():
            print(f"{item}: {price} золота")

    def buy_item(self, player):
        self.show_items()
        item_to_buy = input("Виберіть предмет для покупки (або 'q' для виходу): ")
        if item_to_buy in self.items:
            if player.gold >= self.items[item_to_buy]:
                player.gold -= self.items[item_to_buy]
                self.player_items[item_to_buy] = self.items[item_to_buy]
                print(f"{player.name} купив {item_to_buy}!")
            else:
                print("У вас недостатньо золота.")
        elif item_to_buy == 'q':
            return
        else:
            print("Неправильний вибір предмета.")

def main():
    print("Ласкаво просимо до гри!")
    player_name = input("Введіть ім'я гравця: ")
    player = Player(player_name)
    shop = Shop()

    enemies = [Enemy("Чудовисько", 50, 5), Enemy("Дракон", 100, 10), Enemy("Злодій", 30, 8)]

    while player.is_alive():
        enemy = random.choice(enemies)
        print(f"\nЗ'явився ворог: {enemy.name}")
        player.show_status()

        action = input("Виберіть дію: (1) Атакувати, (2) Спробувати втекти, (3) Відкрити магазин: ")

        if action == "1":
            player_damage = player.attack_enemy(enemy)
            enemy.take_damage(player_damage)

            enemy_damage = enemy.attack_player(player)
            player.take_damage(enemy_damage)
        elif action == "2":
            if random.randint(1, 2) == 1:
                print("Ви втекли від ворога!")
                continue
            else:
                print("Ворог заблокував вашу спробу втекти!")
                enemy_damage = enemy.attack_player(player)
                player.take_damage(enemy_damage)
        elif action == "3":
            shop.buy_item(player)
        else:
            print("Неправильний вибір. Оберіть дію знову.")

    print("Гра закінчена. Ви програли.")

