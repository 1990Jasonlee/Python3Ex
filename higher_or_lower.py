from random import randrange


def high_low():
    random_number = randrange(10)
    guess = int(input("Your guess between 1-10 is: "))
    print(f" The random number was: {random_number}.")

    if random_number > guess:
        print(f"Your guess was {guess}.\n Too low.")
    elif random_number < guess:
        print(f"Your guess was {guess}.\n Too high.")
    elif random_number == guess:
        print(f"Your guess was {guess}.\n You guessed it correctly.")


high_low()
