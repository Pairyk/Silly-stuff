import veff
import json
import random
import time
import entities


def load_game_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"types": ["Adventurer"], "races": ["Human"]}

game_config = load_game_data()


def choose_random_location():
    print("---- Let's Explore around the Island! ----\n")
    veff.traveling_effect()
    current_location = random.choice(game_config["Locations"])
    
    veff.type_write(f"You arrived at: {veff.Y}{current_location['name'].title()}{veff.W}")
    veff.type_write(f"Difficulty: {veff.G}{current_location['difficult']}{veff.W}")
    veff.type_write(f"Local mobs: {veff.R}{current_location['monster_1'].title()}{veff.W}, {veff.R}{current_location['monster_2'].title()}{veff.W}\n")
    
    return current_location

def get_actions(location):
    veff.type_write("Let's see how many actions you get!")
    veff.random_load_effect("Calculating actions...")
    
    diff = int(location["difficult"])
    action_ranges = {1: (1, 4), 2: (2, 5), 3: (3, 6)}
    min_actions, max_actions = action_ranges.get(diff, (1, 1))
    
    action_num = random.randint(min_actions, max_actions)
    veff.type_write(f"You got {action_num} actions!\n")
    return action_num

def get_enemies(action_num, location):
    enemies = [random.choice([location["monster_1"], location["monster_2"]]) for _ in range(action_num)]
    veff.type_write("Enemies encountered: ")
    veff.type_write(", ".join(enemies))
    veff.type_write("")
    return enemies

def battle_action():
    while True:
        print("\nChoose an action:")
        print("1. Attack the enemy")
        print("2. Skip turn")
        print("3. Escape battle")
        
        choice = input("Your choice: ").strip()
        if choice == '1':
            return "attack"
        elif choice == '2':
            return "skip"
        elif choice == '3':
            return "escape"
        else:
            veff.type_write("Invalid action. Try again.")

def enemy_battle(location, enemies, enemy_data, hero):
    veff.type_write(f"\n--- Combat Encounter at {veff.Y}{location['name']}{veff.W} ---\n")
    veff.random_load_effect("Scanning surroundings...")
    
    if isinstance(enemy_data, list):
        enemy_lookup = {}
        for d in enemy_data:
            enemy_lookup.update(d)
    else:
        enemy_lookup = enemy_data

    monsters = [entities.Enemy(name, enemy_lookup[name]) for name in enemies]

    veff.type_write(f"\n{veff.R}Enemies appear!{veff.W}")
    for m in monsters:
        veff.type_write(f"➤ {veff.R}{m.name}{veff.W} | HP: {veff.G}{m.hp}{veff.W}")

    veff.draw_line()

    while hero.is_alive() and any(m.is_alive() for m in monsters):
        veff.type_write(f"{veff.C}{hero.name}'s turn!{veff.W}")
        veff.type_write(f"HP: {veff.G}{hero.hp}/{hero.max_hp}{veff.W} | Attack: {veff.Y}{hero.attack}{veff.W} | Defense: {veff.B}{hero.defense}{veff.W}")
        
        alive_monsters = [m for m in monsters if m.is_alive()]
        veff.type_write("\nEnemies:")
        for i, m in enumerate(alive_monsters, 1):
            veff.type_write(f"{i}. {veff.R}{m.name}{veff.W} | HP: {veff.G}{m.hp}/{m.max_hp}{veff.W}")

        action = battle_action()

        if action == "attack":
            target_index = 0
            if len(alive_monsters) > 1:
                try:
                    target_index = int(input("Choose enemy number to attack: ")) - 1
                    if target_index < 0 or target_index >= len(alive_monsters):
                        target_index = 0
                except:
                    target_index = 0
            target = alive_monsters[target_index]
            veff.type_write(f"{hero.name} attacks {target.name}!")
            target.take_damage(hero.attack)

        elif action == "skip":
            veff.type_write(f"{hero.name} skips the turn.\n")

        elif action == "escape":
            success = random.random() < 0.5
            veff.type_write(f"{hero.name} tries to escape...")
            veff.type_write("Escape successful!" if success else "Escape failed!")
            if success:
                break

        for monster in monsters:
            if monster.is_alive() and hero.is_alive():
                veff.type_write(f"\n{veff.R}{monster.name}'s turn!{veff.W}")
                veff.type_write(f"{monster.name} attacks {hero.name}!")
                hero.take_damage(monster.attack)

        veff.draw_line()
        veff.clear_screen()

    if hero.is_alive():
        veff.type_write(f"\n{veff.G}You survived the battle!{veff.W}")
    else:
        veff.type_write(f"\n{veff.R}{hero.name} has fallen! Game Over.{veff.W}")


def game_round(hero, rounds=1):
    for _ in range(rounds):
        current_location = choose_random_location()
        action_num = get_actions(current_location)
        enemies = get_enemies(action_num, current_location)
        veff.clear_screen()
        enemy_data = game_config["monsters"]
        enemy_battle(current_location, enemies, enemy_data, hero)
        if not hero.is_alive():
            break


if __name__ == "__main__":
    choose_random_location()
    battle_action()
    get_enemies()
    get_actions()
    enemy_battle()
    game_round()
