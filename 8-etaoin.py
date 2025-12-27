def main():
    text = input("Enter a string to generate ETAOIN bar chart: ")

    if not text:
        print("sentence is empty. please enter a valid sentence")

    bar_chart = {}

    for char in text:
        char = char.lower()

        if not char.isalpha():
            continue

        if char not in bar_chart:
            bar_chart[char] = []

        bar_chart[char].append(char)

    sorted_bar_chart = dict(sorted(bar_chart.items()))

    for key, value in sorted_bar_chart.items():
        print(f"{key}: {value}", end="\n")


if __name__ == "__main__":
    main()
