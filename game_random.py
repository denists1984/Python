import random

# generate random num
secret_num = random.randint(1, 10)
print(secret_num)


def game(rest_atmpt = 10):
    while True:
        #get a number guess from the player
        try:
            player_num = int(raw_input("Guess a number between 1 and 10: --> "))
        except ValueError:
            print("Invalid user input. Please enter only numbers!!!")
            print("")
        if player_num in range(1, 10):
        #compare guess to secter numer
            if player_num == secret_num:
                print('Congrads you got it!!! Secret num was {}'.format(secret_num))
                decision = play_again()
                if decision == "Y":
                    game()
                elif decision == 'bad':
                    play_again()
                elif decision == "N":
                    print("Exiting")
                    break
            else:
                rest_atmpt = left_tries(rest_atmpt)
                print("You missed it , Try Again")
                print("You have more {} attempts".format(rest_atmpt))

        else:
            print("Follow the rules!!!!! . Please put a number between 1 and 10")

def left_tries(rest_atmpt):
    if rest_atmpt != 0:
        rest_atmpt = rest_atmpt - 1
        return rest_atmpt
    else:
        print("You have no more attempts to gees the secret number ")
        print("The number ewas - {} !!!".format(secret_num))
        exit

def play_again():
        decision = raw_input("Please Enter 'Y' to play again or 'N' to exit -->"))
        if decision != 'Y' or decision  != 'N':


        print("Unexpected User input")

    return decision


game()

