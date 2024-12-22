from colorama import Fore, Style, init
import time
import random

# Initialize colorama
init(autoreset=True)

# Rainbow colors mapping
RAINBOW_COLORS = {
    "red": Fore.RED,
    "orange": Fore.LIGHTRED_EX,  # Closest to orange
    "yellow": Fore.YELLOW,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "indigo": Fore.LIGHTBLUE_EX,  # Closest to indigo
    "violet": Fore.MAGENTA,  # Closest to violet (purple)
    "purple": Fore.MAGENTA,  # Adding purple explicitly
    "magenta": Fore.MAGENTA,
}

def get_random_color():
    """Returns a random rainbow color."""
    color_name, color_code = random.choice(list(RAINBOW_COLORS.items()))
    return color_name, color_code

def interact():
    """Handles the user interaction loop."""
    while True:
        user_input = input("Type 'hello' to interact or 'exit'/'quit'/'later' to quit: ").lower()

        if user_input == "hello":
            color = input("What's your favorite color? ").lower()

            if color in RAINBOW_COLORS:
                message = f"{color.capitalize()}: Me too!" if color == "purple" else f"{color.capitalize()}: That's an interesting choice!"
                print(RAINBOW_COLORS[color] + message)
            elif color == "random":
                random_color, random_code = get_random_color()
                print(random_code + f"Surprise! How about {random_color.capitalize()}?")
            else:
                print(Style.DIM + f"{color.capitalize()}: That's not in the rainbow, but it's still cool!")

        elif user_input in ["exit", "quit", "later"]:
            print("Exiting the program. Later!")
            time.sleep(3)
            break

        else:
            print("Invalid input! Type 'hello' to interact or 'exit'/'quit'/'later' to quit.")

# Start interaction
interact()
