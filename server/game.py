import random

options = ["snake", "water", "gun"]
winCases = {
    (0, 2),
    (1, 0),
    (2, 1),
}


if __name__=='__main__':
    def main():
        for index, option in enumerate(options):
            print(f"{index}: {option}")

        userChoice = int(input("Enter your choice (integer): "))
        compChoice = random.randint(0, 2)

        if compChoice == userChoice:
            print("Draw")
            return 0

        elif (compChoice, userChoice) in winCases:
            print("Win")
            return 1

        else:
            print("You lost")
            return -1

    main()