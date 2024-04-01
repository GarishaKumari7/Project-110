import random
response=str("y")

while response=="y":
    roll_dice= input("Do you want to roll the dice (y/n):")

    if roll_dice.lower()=='y':
        dice_roll = random.randint(1, 6)
        no=random.randint(1, 6)
        
        # Use the value of 'no' to print the output representing the dice
        if no == 1:
            print("---------")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("---------")
        elif no == 2:
            print("---------")
            print("| *     |")
            print("|       |")
            print("|     * |")
            print("---------")
        elif no == 3:
            print("---------")
            print("| *     |")
            print("|   *   |")
            print("|     * |")
            print("---------")
        elif no == 4:
            print("---------")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("---------")
        elif no == 5:
            print("---------")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("---------")
        elif no == 6:
            print("---------")
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
            print("---------")
        
        response = input("Do you want to roll the dice again? (y/n): ")
    elif roll_dice.lower() == 'n':
        print("Okay, goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' to roll the dice or 'n' to exit.")
        response = input("Do you want to roll the dice (y/n): ")
