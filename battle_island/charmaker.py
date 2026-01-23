import random
import veff

# |----------| UP IS LIBRARIES |----------| DOWN IS NAME GETTER |----------|


def get_name():
    while True:
        name_input = input("\nHero Name or random: ").strip()

        if name_input.lower() == "random":
            veff.random_load_effect("Generating Name")

            consonants = "qwrtypsdfghjklzxcvbnm"
            vowels = "euioa"
            length = random.randint(3, 8)

            name = "".join(random.choice(consonants if i % 2 == 0 else vowels) for i in range(length)).capitalize()
        elif name_input.isalpha() and len(name_input) > 2:
            name = name_input.capitalize()
        else:
            print(f"{veff.R}Only letters & No less than two letters!{veff.W}")
            continue

        print(f"{veff.G}>> HERO CREATED: {veff.W}{veff.Y}{name}{veff.W}")
        veff.clear_screen()
        return name
    

# |----------| UP IS NAME GETTER |----------| DOWN IS LIST CHOICER |----------|


def get_choice_from_list(label, data_list):
    while True:
        veff.draw_line()
        print(f"{veff.C} {label.upper().center(35)} {veff.W}")
        veff.draw_line()

        for i, item in enumerate(data_list, 1):
            entry = f"{i:2}. {veff.B}{item:<15}{veff.W}"
            print(entry, end="\n" if i % 2 == 0 else " ")

        user_input = input(f"Choose {label} (or 'random'): ").strip().title()

        if user_input.lower() == "random":
            veff.random_load_effect(f"Choosing {label}")
            choice = random.choice(data_list)
            print(f"{veff.G}>> Result: {choice}!{veff.W}")
            veff.clear_screen()
            return choice
        
        if user_input.isdigit():
            selection = int(user_input)
            if 1 <= selection <= len(data_list):
                choice = data_list[selection - 1]
                print(f"{veff.G}>> Selected: {choice}{veff.W}")
                veff.clear_screen()
                return choice

        if user_input in data_list:
            print(f"{veff.G}>> Result: {user_input}!{veff.W}")
            veff.clear_screen()
            return user_input
        
        print(f"{veff.R}!! '{user_input}' is not on the list. Try again.{veff.W}")
        veff.clear_screen()


# |----------| UP IS LIST CHOICER |----------| DOWN IS NUMERIC GETTER |----------|


def get_numeric_input(label, min_val, max_val):
    while True:
        veff.draw_line()
        user_input = input(f"Enter {label} [{min_val}-{max_val}] (or 'random'): ").strip().lower()

        if user_input == "random":
            veff.random_load_effect(f"Calculating {label}")
            val = random.randint(min_val, max_val)
            print(f">> Result: {val}")
            veff.clear_screen()
            return val
        
        if user_input.isdecimal():
            val = int(user_input)
            if min_val <= val <= max_val:
                veff.clear_screen()
                return val
        
        print(f"!! Please enter a number between {min_val} and {max_val}.")
        veff.clear_screen()


# |----------| UP IS NUMERIC GETTER |----------| DOWN IS STAT GETTER |----------|


def get_stats(hero):
    while True:
        print("\nLet's add some points to stats!")
        hero.display_stats()

        stat_name = input("Which stat to increase(exit | random): ")

        if stat_name == "exit":
            hero.display_stats()
            hero.display_profile()
            break
        elif stat_name == "random":
            veff.clear_screen()

            stat_names = list(vars(hero.stats))

            while hero.point_pool > 0:
                print(f"Gambling your {hero.point_pool} points")
                target_stat = random.choice(stat_names)

                amount = random.randint(1, min(3, hero.point_pool))
                hero.apply_stats(target_stat, amount)
                veff.clear_screen()

            hero.display_stats()
            break
        elif stat_name.isalpha():
            amount = int(input("How much points to put: "))

            if amount > hero.point_pool:
                print(f"{veff.R}You have only {hero.point_pool} points{veff.W}")
                veff.clear_screen()
                continue
            else:
                hero.apply_stats(stat_name, amount)
                veff.clear_screen()
        else:
            print(f"{veff.R}No numbers!{veff.W}")
            veff.clear_screen()

# |----------| UP IS STAT GETTER |----------| DOWN IS LAUNCH BUTTON |----------|


if __name__ == "__main__":
    get_name()
    get_choice_from_list()
    get_numeric_input()
    get_stats()
