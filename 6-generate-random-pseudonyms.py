import random

from colorama import Fore, init

init(autoreset=True)


def main():
    first_name = ("Sweet Tea", "Tee Tee")
    last_name = ("Appleyar", "Bigmeat")

    while True:
        pseudo_first = random.choice(first_name)
        pseudo_second = random.choice(last_name)

        print(Fore.RED + pseudo_first, Fore.RED + pseudo_second)

        play_again = input("Try again? Press enter or y else type n to exit: ")

        if play_again.lower() == "n":
            break

    print("Game over! See you soon!!")
    input("Press Enter to exit")


if __name__ == "__main__":
    main()
