def chatBotSystem():
    print("Enter Your Name : ", end="")
    name = input()
    print("Hello " + name + " Welcome to MET-Restaurant\n")
    print("What would you like to order " + name + " \n")

    menuOptions = ["Rice-Plate", "Samosa", "Vada-Pava", "Chole-Bhature", "Pohe"]
    qCount = [0] * len(menuOptions)
    while True:
        for i, option in enumerate(menuOptions, 1):
            print("Option " + str(i) + " : " + option)

        opt = int(input("\nI would like to have option : "))
        if opt < 1 or opt > len(menuOptions):
            print("Please enter a valid option\n")
            continue
        print("\nYou Confirm order : " + menuOptions[opt - 1])
        qCount[opt - 1] += 1
        if qCount[opt - 1] >= 5:
            break

        order = input("Do you want anything else (yes/no): ").strip().lower()
        print()
        if order == "yes":
            continue
        elif order == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'\n")

    yourOrder(menuOptions, qCount)
    print("\nYour total bill is " + str(totalBill(qCount)))
    print("\nThanks for your order!")


def totalBill(qCount):
    prize = [50, 25, 25, 55, 25]
    return sum(qCount[i] * prize[i] for i in range(len(qCount)))


def yourOrder(menuOptions, qCount):
    print("Your Order is : ")
    for i, count in enumerate(qCount):
        if count > 0:
            print(menuOptions[i] + " " + str(count))


if __name__ == "__main__":
    chatBotSystem()
