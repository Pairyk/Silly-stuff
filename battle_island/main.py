import json
import entities
import charmaker
import veff
import engine

def load_game_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"types": ["Adventurer"], "races": ["Human"]}

game_config = load_game_data()


def character_creation():
    name = charmaker.get_name()
    gender = charmaker.get_choice_from_list("Gender", ["Male", "Female"])
    type = charmaker.get_choice_from_list("Class", game_config["types"])
    race = charmaker.get_choice_from_list("Race", game_config["races"])

    hero = entities.Hero(name, gender, type, race)
    hero.display_profile()
    charmaker.get_stats(hero)

    return hero


def main_menu(hero):
    while True:
        print(f"--- {veff.Y}THE MAIN MENU{veff.W} ---", end = "\n\n")
        print("1. Start The Journey")
        print("2. Check Character Stats")
        print("3. Check Character Profile")

        user_choice = input(f"\n{veff.C}What to do: {veff.W}")
        
        if user_choice == "1":
            veff.clear_screen()
            break
        elif user_choice == "2":
            hero.display_stats()
            veff.clear_screen()
        elif user_choice == "3":
            hero.display_profile()
            veff.clear_screen()
        else:
            print(f"{veff.R}Please enter valid numbers!{veff.W}")
            veff.clear_screen()
            continue


def beginning_scene(hero):
    veff.type_write(f"Hello, {"Hero" if hero.gender == "Male" else "Heroine"} {hero.name}! You are on the Ancient Island! Survive or Die!\n")
    veff.type_write(f"The Island contains magical crystals that can grant you forgotten by world magic...\n")
    veff.type_write(f"Find them and show the Island Keepers why you were named hero after all!\n")
    veff.type_write(f"For {hero.race}'s! For {hero.hero_class}'s! For The Kingdom!\n")
    veff.clear_screen()


def main():
    veff.draw_banner()
    print(f"Welcome to the {veff.Y}Battle Island!{veff.W}\nTo start the game you should create a {veff.Y}Hero!{veff.W}\n\nPress enter to create a character...")
    
    hero = character_creation()
    veff.clear_screen()

    main_menu(hero)
    beginning_scene(hero)

    rounds = int(input("How many rounds: "))
    
    engine.game_round(hero, rounds)


if __name__ == "__main__":
    main()
