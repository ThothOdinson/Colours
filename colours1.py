from colorama import Fore, Style, init
import time

# Initialize colorama
init(autoreset=True)

# Rainbow colors mapping
rainbow_colors = {
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

while True:
    user_input = input("Type 'hello' to interact or 'later' or 'exit' or 'quit' to quit: ").lower()

    if user_input == "hello":
        color = input("What's your favorite color? ").lower()

        if color in rainbow_colors:
            if color == "purple":
                print(rainbow_colors[color] + f"{color.capitalize()}: Me too!")
            else:
                print(rainbow_colors[color] + f"{color.capitalize()}: That's an interesting choice!")
        else:
            print(Style.DIM + f"{color.capitalize()}: That's not in the rainbow, but it's still cool!")

    elif user_input in ['exit', 'quit', 'later']:
        print("Exiting the program. Later!")
        time.sleep(3)
        break
    
    else:
        print("Wrong! Type 'hello' to interact or 'later' or 'exit' or 'quit' to quit.")