a = int(input("Enter a number between 1 to 10: "))

match a:
    case 1:
        print("You won a Macbook Air")
    case 3:
        print("You won a Airpods Gen4")
    case 6:
        print("You won an iPhone SE")
    case _:
        print("Better Luck! Try next time.")