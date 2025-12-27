import random

from colorama import Fore, init

init(autoreset=True)


def generate_name(first_name, second_name):
    return (random.choice(first_name), random.choice(second_name))


def main():
    first_name = ("Sweet Tea", "Tee Tee")
    second_name = ("Appleyar", "Bigmeat")

    if not first_name or not second_name:
        return "Sorry, our name list is temporarorily out of names. Come back later!"

    while True:
        pseudo_first, pseudo_second = generate_name(first_name, second_name)

        print(Fore.RED + pseudo_first, Fore.RED + pseudo_second)

        while True:
            play_again = input(
                "Try again? Press enter or y else type n to exit: "
            ).lower()

            if play_again == "n":
                should_continue = False
                break
            elif play_again == "y" or play_again == "":
                should_continue = True
                break
            else:
                print("Plese enter 'y' or 'n'")
                continue

        if not should_continue:
            break

    print("Game over! See you soon!!")
    input("Press Enter to exit")


if __name__ == "__main__":
    main()
