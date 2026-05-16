import random
def continuity(game_continue, player_hp, enemy_hp):
    if player_hp == 0 or enemy_hp == 0:
        game_continue = "False"
    elif player_hp == 0 and enemy_hp == 0:
        game_continue = "False"
    else:
        game_continue = "True"
def combat_attack(player_element):
    if player_element == "fire":
        attack_type_fire(player_element, enemy_hp, player_hp)
def attack_type_fire(player_element, enemy_hp, player_hp):
    if player_element == "fire":
        attack_types = input(
            "Which attack will you use? Phoenix Blow (burns you and enemy), Fireball (a light attack), or Punch (a punch)? ").lower()
        if attack_types == "phoenix blow":
            enemy_hp -= 10
            print("You used Phoenix Blow! You and the enemy both take burn damage.")
            enemy_hp = player_effect(player_element, enemy_hp)
        elif attack_types == "fireball":
            enemy_hp -= 5
            enemy_hp = player_effect(player_element, enemy_hp)
            print("You used Fireball! Enemy HP is now:", enemy_hp)
        elif attack_types == "punch":
            enemy_hp -= 3
            print("You punched the enemy! Enemy HP is now:", enemy_hp)
        else:
            print("Invalid attack choice. You wasted your turn.")


def player_effect(player_element, enemy_hp):
    if player_element == "fire":
        print("The enemy burned!")
        enemy_hp = enemy_hp-2
    elif player_element == "water":
        water_death = random.randint(1, 50)
        if water_death == 1:
            print("The enemy drowned!")
            enemy_hp = 0
        else:
            print("The enemy survived the water!")


print("Game Guide: Welcome to the battle arena. Here you will fight using elemental abilities")
player_name = input("Game Guide: What is your name, fighter? ")
player_element =  input(f"Game Guide: Well then, {player_name}. Now is the time to pick your element. Fire, Water, Earth or Air?(if you cannot decide, put other in the input section) ")
player_element_lower = player_element.lower()
if player_element_lower == "fire":
    element = "fire"
    print(f"You have picked the element of {element}.")
elif player_element_lower == "water":
    element = "water"
    print(f"You have picked the element of {element}.")
elif player_element_lower == "earth":
    element = "earth"
    print(f"You have picked the element of {element}.")
elif player_element_lower == "air":
    element = "air"
    print(f"You have picked the element of {element}.")
else:
    print("Well, I cannot know this choice so, I will give you an element from randomness.")
    random_element = random.randint(1, 4)
    if random_element == 1:
      print("Your element is, fire!")
      element = "fire"
    elif random_element == 2:
        print("Your element is water!")
        element = "water"
    elif random_element == 3:
        print("Your element is earth!")
        element = "earth"
    elif random_element == 4:
        print("Your element is air!")
        element = "air"
print(f"{player_name}, you have unlocked {element}, now you will meet the people who you will live, fight with and fight.")
print("Here is your rival dude.")
rival_name = input(f"Rival Guy: Sup dude, your name is {player_name}, right? Well, call me whatever you want. ")
rival_element_selector = random.randint(1, 4)
if rival_element_selector == 1:
    rival_element = "fire"
    print(f"{rival_name}: You got {element}? Well, I picked {rival_element}.")
elif rival_element_selector == 2:
    rival_element = "water"
    print(f"{rival_name}: You got {element}? Well, I picked {rival_element}.")
elif rival_element_selector == 3:
    rival_element = "earth"
    print(f"{rival_name}: You got {element}? Well, I picked {rival_element}.")
elif rival_element_selector == 4:
    rival_element = "air"
    print(f"{rival_name}: You got {element}? Well, I picked {rival_element}.")
print(f"{player_name}, you will now fight your first opponent. He uses fire. Each element has its own effect.")
player_hp = 100
enemy_hp = 20
game_continue = "True"
enemy_picker = random.choice(["fire", "water", "earth", "air"])
print(f"{player_name}, this is your first fight, your first enemy is a monkey, it has the element of {enemy_picker}. The monkey will assault you.")
while game_continue == "True"
    continuity(game_continue, player_hp, enemy_hp)
    if game_continue == "False":
        break

    player_attack = str(input("Will you attack(attacks enemies) or defend(stops damage)? ")).lower()
    if player_attack == "attack":
        attack_types = "not yet"
        combat_attack(player_element)

