import random
from pyfiglet import figlet_format
from shutil import get_terminal_size


from os import system, name
def clear_screen():
    system("cls" if name == "nt" else "clear")

location = "village"
running = True
game_state = "normal"
current_enemy = None
player = None

def başlık(location):
    print(figlet_format(location.upper()))
    print("\n" * 5)


class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.health = 30
        self.attack = 8
        self.defense = 2
        self.xp = 10
    def take_damage(self, damage):
        self.health -= damage

class Skeleton:
    def __init__(self):
        self.name = "Skeleton"
        self.health = 20
        self.attack = 15
        self.defense = 1
        self.xp = 15
    def take_damage(self, damage):
        self.health -= damage

class Zombie:
    def __init__(self):
        self.name = "Zombie"
        self.health = 50
        self.attack = 12
        self.defense = 5
        self.xp = 25
    def take_damage(self, damage):
        self.health -= damage
    

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []
        self.gold = 50
        self.max_health = 100
        self.xp = 0
        self.next_level = 100
        self.level = 1
        self.weapon = None
        self.armor = None
    def take_damage(self, damage):
        self.health -= damage
    def gainxp(self, amount):
        self.xp += amount
        if self.xp >= self.next_level:
            self.level += 1
            self.next_level += 100
            self.attack += 5
            self.defense += 1
            self.max_health += 20

class Shop:
    def __init__(self,name):
        self.name = name
        self.inventory = []
    def fill_Smith_inventory(self):
        for i in range (10):
            Smithchance = random.randint(0 , 1)
            if Smithchance == 0:
                self.inventory.append(Wooden_Sword)
            if Smithchance == 1:
                self.inventory.append(Regular_Armor)
    def fill_Alchemist_inventory(self):
        for i in range (10):
            self.inventory.append(Health_Potion)
    def clear_inventory(self):
        self.inventory.clear()

Smith = Shop("Smith")
Alchemist = Shop("Alchemist")
current_shop = None



class Potion:
    def __init__(self):
        self.name = "Potion"
        self.heal_amount = 20
        self.item_type = "consumable"
        self.cost = 10
        self.sellcost = 5
    def use(self, player):
        player.health += self.heal_amount
        if player.health > player.max_health:
            player.health = player.max_health

class Sword:
    def __init__(self,name,AD,cost,sellcost):
        self.name = name
        self.AD = AD
        self.cost = cost
        self.sellcost = sellcost
        self.item_type = "equipment"
    def equip(self, player):
        if player.weapon is not None:
            player.attack -= player.weapon.AD
            player.inventory.append(player.weapon)

        player.weapon = self
        player.attack += self.AD 
        


class Armor:
    def __init__(self, name, hp, armor, cost, sellcost):
        self.name = name
        self.health = hp
        self.armor = armor
        self.cost = cost
        self.sellcost = sellcost
        self.item_type = "equipment"
    def equip(self, player):
        if player.armor is not None:
            player.defense -= player.armor.armor
            player.max_health -= player.armor.health
            player.inventory.append(player.armor)

        player.armor = self
        player.defense += self.armor
        player.max_health += self.health

Health_Potion = Potion()
Wooden_Sword = Sword("Wooden Sword", 10, 15, 10)
Regular_Armor = Armor("Regular Armor", 25, 7, 20, 15)
Smith.fill_Smith_inventory()
Alchemist.fill_Alchemist_inventory()

def show_player_stats(player):
    terminal_width = get_terminal_size().columns

    print(f"Name: {player.name}".rjust(terminal_width))
    print(f"HP: {player.health}".rjust(terminal_width))
    print(f"MaxHP: {player.max_health}".rjust(terminal_width))
    print(f"Attack: {player.attack}".rjust(terminal_width))
    print(f"Defense: {player.defense}".rjust(terminal_width))
    print(f"Gold: {player.gold}".rjust(terminal_width))
    print(f"XP: {player.xp}".rjust(terminal_width))
    print(f"Next Level: {player.next_level}".rjust(terminal_width))
    print(f"Level: {player.level}".rjust(terminal_width))
    if player.weapon:
        print(f"Weapon: {player.weapon.name}".rjust(terminal_width))
    if player.armor:
        print(f"Armor: {player.armor.name}".rjust(terminal_width))
    


Name = input("Enter your character's name: ")
player = Player(Name)

combat_log = ""
message = ""

def show_message():
    global message
    if message:
        print(message)
        print()
        message = ""

while running:
    clear_screen()
    show_player_stats(player)
    if game_state == "normal":
        if location == "village":
            başlık("Village")
            print("You are in the village.")
            print("1. Go to the forest")
            print("2. Go to the cave")
            print("3. Go home")
            print("4. Quit")
            print("5. Go to the market")
            choice = input("What do you want to do? ")
            if choice == "1":
                print("You go to the forest.")
                location = "forest"
            elif choice == "2":
                print("You go to the cave.")
                location = "cave"
            elif choice == "3":
                print("You go home.")
                location = "home"
            elif choice == "4":
                print("You quit the game.")
                running = False
            elif choice == "5":
                location = "market"
            else:
                print("Invalid choice.")
        elif location == "forest":
            goblin_chance = random.randint(1, 100)
            başlık("Forest")
            show_message()
            if goblin_chance <= 30:
                game_state = "Encounter"
                current_enemy = Goblin()
                continue
            print("You are in the forest")
            print("1. Go to the village")
            print("2. Go to the cave")
            print("3. Fight a goblin")
            print("4. Quit")
            choice = input("What do you want to do? ")
            if choice == "1":
                print("You go to the village.")
                location = "village"
            elif choice == "2":
                print("You go to the cave.")
                location = "cave"
            elif choice == "3":
                goblin_chance = random.randint(1, 100)
                if goblin_chance <= 30:
                    game_state = "Encounter"
                    current_enemy = Goblin()
                    continue
            elif choice == "4":
                print("You quit the game.")
                running = False
            else:
                print("Invalid choice.")
        elif location == "cave":
            enemy_chance = random.randint(1, 100)
            başlık("Cave")
            show_message()
            if enemy_chance <= 30:
                game_state = "Encounter"
                sorz = random.randint(0, 1)
                if sorz == 0:
                    current_enemy = Skeleton()
                if sorz == 1:
                    current_enemy = Zombie()
                continue
            print("You are in the cave.")
            print("1. Go to the village")
            print("2. Go to the forest")
            print("3. Fight an enemy")
            print("4. Quit")
            choice = input("What do you want to do? ")
            if choice == "1":
                print("You go to the village.")
                location = "village"
            elif choice == "2":
                print("You go to the forest.")
                location = "forest"
            elif choice == "3":
                game_state = "Encounter"
                sorz = random.randint(0, 1)
                if sorz == 0:
                    current_enemy = Skeleton()
                if sorz == 1:
                    current_enemy = Zombie()
                continue
            elif choice == "4":
                print("You quit the game.")
                running = False
            else:
                print("Invalid choice.")
        elif location == "home":
            başlık("Home")
            show_message()
            print("You are at home.")
            print("1. Go to the village")
            print("2. Go to sleep")
            print("3. View inventory")
            print("4. Quit")
            choice = input("What do you want to do? ")
            if choice == "1":
                print("You go to the village.")
                location = "village"
            elif choice == "2":
                player.health = player.max_health
                message = "You go to sleep.\nYou wake up feeling refreshed."
                location = "home"
            elif choice == "3":
                game_state = "Inventory"
                continue
            elif choice == "4":
                print("You quit the game.")
                running = False
        elif location == "market":
            başlık("Market")
            show_message()
            print("You are at the market")
            print("1. Return to the village")
            print("2. Go to Smith")
            print("3. Go to Alchemist")
            choice = input("What do you want to do? ")
            if choice == "1":
                print("You return to the village.")
                location = "village"
            if choice == "2":
                current_shop = Smith
                game_state = "Shop"
                continue
            if choice == "3":
                current_shop = Alchemist
                game_state = "Shop"
                continue
    if game_state == "Encounter":
        başlık("Encounter")
        print(f"A wild {current_enemy.name} appears!")
        print("1. Fight")
        print("2. Run")
        choice = input("What do you want to do? ")
        if choice == "1":
            game_state = "Combat"
            continue
        elif choice == "2":
            print(f"You run away from the {current_enemy.name}.")
            game_state = "normal"
            continue
        else:
            print("Invalid choice.")
    if game_state == "Combat":
        başlık("Combat")
        print(f"You are fighting a {current_enemy.name}!")
        print(f"Your health: {player.health}")
        print(f"{current_enemy.name}'s health: {current_enemy.health}")

        print()
        print(combat_log)
        print() 

        print("1. Attack")
        print("2. Run")
        choice = input("What do you want to do? ")
        if choice == "1":
            damage = player.attack - current_enemy.defense
            if damage < 0:
                damage = 0
            current_enemy.take_damage(damage)
            combat_log += f"You attack the {current_enemy.name} for {damage} damage!\n"
            if current_enemy.health <= 0:
                lootchance = random.randint(0,2)
                message = f"You have defeated the {current_enemy.name}!\n"
                message += "You gained 25 Gold!\n"
                message += f"You gained {current_enemy.xp} XP!\n"

                if lootchance == 0:
                    player.inventory.append(Health_Potion)
                    message += "You found a Health Potion!"
                if lootchance == 1:
                    player.inventory.append(Wooden_Sword)
                    message += "You found a Wooden Sword!"
                if lootchance == 2:
                    player.inventory.append(Regular_Armor)
                    message += "You found a Regular Armor!"

                player.gold += 25
                player.gainxp(current_enemy.xp)

                game_state = "normal"
                current_enemy = None
                combat_log = ""
                continue
            enemy_damage = current_enemy.attack - player.defense
            if enemy_damage < 0:
                enemy_damage = 0   
            player.take_damage(enemy_damage)
            combat_log += f"The {current_enemy.name} attacks you for {enemy_damage} damage!\n"
            if player.health <= 0:
                combat_log += "You have been defeated!"
                running = False
        if choice == "2":
            combat_log += f"You run away from the {current_enemy.name}."
            game_state = "normal"
            current_enemy = None 
            combat_log = ""

    if game_state == "Inventory":
        başlık("Inventory")
        show_message()
        if not player.inventory:
            print("Your inventory is empty.")
            print("0. Go back")
        else:
            print("0. Go back")
            for index, item in enumerate(player.inventory, start=1):
                print(f"{index}. {item.name}")  
        print()
        choice = input("What do you want to do? ")

        if choice == "0":
            game_state = "normal"
            continue
        else: 
            choice = int(choice)
            if choice < 1 or choice > len(player.inventory):
                message = "Invalid choice."
                continue
            item = player.inventory[choice - 1]
            if item.item_type == "consumable":
                item.use(player)
                player.inventory.remove(item)
                message = f"You used a {item.name} and restored {item.heal_amount} health."
            if item.item_type == "equipment":
                item.equip(player)
                player.inventory.remove(item)
                message =f"You equipped {item.name}"
            continue
    if game_state == "Shop":
        başlık(current_shop.name)
        show_message()
        column_width = 35

        print(f"{'YOUR INVENTORY':<{column_width}}{'SHOP INVENTORY'}")
        print()

        max_rows = max(len(player.inventory), len(current_shop.inventory))

        for i in range(max_rows):
            left = ""
            right = ""

            if i < len(player.inventory):
                left = f"{i + 1}. {player.inventory[i].name}"

            if i < len(current_shop.inventory):
                right = f"{i + 1}. {current_shop.inventory[i].name:<{15}}  {current_shop.inventory[i].cost} Gold"

            print(f"{left:<{column_width}}{right}")

        print()
        print("0. Go back")
        print("1. Buy")
        print("2. Sell")
        choice = input("What do you want to do?")
        if choice == "0":
            message = "You go back to the market"
            location = "market"
            game_state = "normal"
            continue
        if choice == "1":
            number = input("Which item do you want to buy?")
            item = current_shop.inventory[int(number) - 1]
            if player.gold >= item.cost:
                player.gold -= item.cost
                player.inventory.append(item)
                current_shop.inventory.remove(item)
            else:
                message = "You don't have enough gold"
                continue
        if choice =="2":
            number = input("Which item do you want to sell?")
            item = player.inventory[int(number) - 1]
            player.gold += item.sellcost
            player.inventory.remove(item)
            current_shop.inventory.append(item)
            message = f"You sold {item.name}"
            continue

                




