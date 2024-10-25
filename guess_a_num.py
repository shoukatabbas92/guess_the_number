import random


def guess_a_number():
    number = random.randint(1,100)
    attemps = 0
     

    while True:
        guess = int(input("Guess a number Between 1 to 100: "))
        attemps += 1


        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Congrations! You guessed the number in {attemps} attemps.")
            break

guess_a_number()
