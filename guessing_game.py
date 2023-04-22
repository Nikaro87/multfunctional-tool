import random
def guessing_game():
    tryes = 1
    print("The number is 1-20!!!!!!!!!!!")
    number = random.randint(1 , 20)

    while True:
        player_input = int(input("What number you choose\n"))
        if player_input < number:
            print("The number is higher!")
            tryes = tryes + 1
            print(tryes)
        elif player_input > number:
            print("The number is lower!")
            tryes = tryes + 1
            print(tryes)
        if tryes == 5:
            print("You failed!")
            break
        if player_input == number:
            print("You did it!")
            break







