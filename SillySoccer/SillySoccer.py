import csv
import random
import time
import os

def power_bar(symbol, value):
    if value <= 0:
        return "-"
    return symbol * value

def get_match_info():
    clubs = ["Bogde", "Maunt"]

    while True:
        try:
            first_team = input("The first club: ").strip().title()
            second_team = input("The second club: ").strip().title()
            rounds = int(input("How many rounds: "))
        except ValueError:
            print("Invalid data type! Please enter a number for rounds.")
        else:
            if rounds <= 0:
                print("Match must have at least 1 round!")
                continue

            if not {first_team, second_team}.issubset(clubs):
                print(f"No such club! Available: {', '.join(clubs)}")
                continue
            elif first_team == second_team:
                print("Clubs can't be similar!")
                continue
            return first_team, second_team, rounds

def get_players(club):
    players = []
    filename = club + "FC.csv"
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:

                players.append({
                    "name": row.get("name", "Unknown Player"), 
                    "position": row.get("position", "Unknown")
                })
        return players
    except FileNotFoundError:
        print(f"Error: {filename} not found in {script_dir}")
        return []

def main():

    first_club, second_club, rounds = get_match_info()

    first_club_info = get_players(first_club)
    second_club_info = get_players(second_club)

    if not first_club_info or not second_club_info:
        print("Could not load player data. Exiting.")
        return

    first_club_names = [p["name"] for p in first_club_info]
    second_club_names = [p["name"] for p in second_club_info]
    
    all_names = first_club_names + second_club_names
    scores = {name: 0 for name in all_names}
    saves = {name: 0 for name in all_names}
    

    first_gk = next((p["name"] for p in first_club_info if p["position"] == "GK"), first_club_names[-1])
    second_gk = next((p["name"] for p in second_club_info if p["position"] == "GK"), second_club_names[-1])

    first_club_goals = 0
    second_club_goals = 0


    for r in range(rounds):
        print(f"\n===== ROUND {r + 1} =====")
        time.sleep(1)

        attacker_one = random.choice(first_club_names)
        attacker_two = random.choice(second_club_names)

        p1_stat = random.randint(1, 5)
        p2_stat = random.randint(1, 5)

        print(f"{attacker_one} power: {p1_stat}")
        print(f"{attacker_two} power: {p2_stat}\n")

        if p1_stat == p2_stat:
            print("Players cancel each other out. Midfield battle continues...")
            time.sleep(2)
            continue


        if p1_stat > p2_stat:
            attacker = attacker_one
            defender = attacker_two
            attack_power = p1_stat - p2_stat
            gk_name = second_gk
            gk_stat = random.randint(0, 2)
            attacking_team = first_club
        else:
            attacker = attacker_two
            defender = attacker_one
            attack_power = p2_stat - p1_stat
            gk_name = first_gk
            gk_stat = random.randint(0, 2)
            attacking_team = second_club

        print(f"{attacker} outplays {defender}!")
        print(f"Shot power : {power_bar('#', attack_power)} ({attack_power})")
        print(f"GK reaction: {power_bar('#', gk_stat)} ({gk_stat})")
        time.sleep(2)

        if attack_power > gk_stat:
            print(f"GOAL! {attacker} scores for {attacking_team}!")
            scores[attacker] += 1
            if attacking_team == first_club:
                first_club_goals += 1
            else:
                second_club_goals += 1
        else:
            print(f"SAVE! {gk_name} denies the goal!")
            saves[gk_name] += 1
        
        time.sleep(2)

    print("\n" + "="*25)
    print("      FINAL SCORE")
    print("="*25)
    print(f"{first_club}: {first_club_goals}")
    print(f"{second_club}: {second_club_goals}")
    print("="*25)

    if first_club_goals > second_club_goals:
        print(f"WINNER: {first_club.upper()}!")
    elif second_club_goals > first_club_goals:
        print(f"WINNER: {second_club.upper()}!")
    else:
        print("RESULT: IT'S A DRAW!")

    print("\n===== TOP SCORERS =====")
    for player, goals in scores.items():
        if goals > 0:
            print(f"{player}: {goals} Goal(s)")

    print("\n===== TOP KEEPER SAVES =====")
    for keeper in [first_gk, second_gk]:
        print(f"{keeper}: {saves[keeper]} Save(s)")

if __name__ == "__main__":
    main()
