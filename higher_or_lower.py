from random import randrange

def high_low():

    random_number = randrange(10)
    guess = int(input("Your guess between 1-10 is: "))
    print(f" The random number was: {random_number}.")

    if random_number > guess:
        print(f"Your guess was {guess}. Too high.")