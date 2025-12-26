def main():
    while True:
        input_word = input("please enter a word to see its pig latin form: ")

        if len(input_word) == 0:
            print("please enter a proper word")
            continue

        starting_letter = input_word[0]
        vowels = "aeiou"

        if starting_letter not in vowels:
            latin_pig = input_word[1:] + starting_letter + "ay"
        else:
            latin_pig = input_word + "way"

        print(latin_pig)

        try_again = input("Want to try another word? Press enter or else enter n: ")

        if try_again.lower() == "n":
            break


if __name__ == "__main__":
    main()
    input("thank you for playing!")
