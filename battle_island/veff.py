import os
import time

# --- COLOR CODES ---
R = "\033[0;31m"    # Red (Errors)
G = "\033[0;32m"    # Green (Success)
Y = "\033[1;33m"    # Yellow (Highlights/Gold)
B = "\033[1;34m"    # Blue (Information)
C = "\033[1;36m"    # Cyan (Names/Labels)
W = "\033[0m"       # White (Reset)

def draw_line(pos: str =" ", width: int = 40):
    if pos == "up":
        print(f"┏{'━' * width}┓")
    elif pos == "down":
        print(f"┗{'━' * width}┛")
    else:
        print(f"{'━' * width}")

def draw_banner():
    os.system('cls' if os.name == "nt" else 'clear')
    print(f"┏" + "━" * 100 + "┓")
    print(f"┃{C}{'BATTLE ISLAND'.center(100)}{W}┃")
    print(f"┃{C}{'VERSION 1.3'.center(100)}{W}┃")
    print(f"┗" + "━" * 100 + f"┛")

def random_load_effect(action="Randomizing"):
    print(f"\n{C}{action}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(f'{W}\n')    

def clear_screen():
    print(f"\nPress Enter to continue...")
    input()
    os.system('cls' if os.name == "nt" else 'clear')
    draw_banner()

def type_write(text):
    for i, letter in enumerate(text, 1):
        time.sleep(0.05)
        if i == len(text):
            print(letter, end="\n", flush=True)
        else:
            print(letter, end="", flush=True)

def traveling_effect(total=50):
    for i in range(0,total+1,10):
        percent = (i/50)*100
        bar = '█' * i + '░' * (total - i)
        print(f"Traveling: |{bar}| {percent:.1f}%\n", end="", flush=True)
        time.sleep(0.7)
        clear_screen()

if __name__ == "__main__":
    draw_banner()
    draw_line()
    random_load_effect()
    clear_screen()
    type_write()
