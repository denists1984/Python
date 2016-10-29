import random

# generate random num
secret_num = random.randint(1, 10)
print(secret_num)

def game():

    while True:
        #get a number guess from the player
        player_num = int(raw_input("Guess a number between 1 and 10: --> "))
        if player_num in range(1, 10):
        #compare guess to secter numer
            if player_num == secret_num:
                print("Congrads you got it!!! Secret num was {}".format(secret_num))
                break
            else:
                print("You missed it , Try Again")
        else:
            print("Follow the rules!!!!! . Please put a number between 1 and 10")

def tries():
    tries = 10
    if tries != 0:
        tries = (tries -1)
