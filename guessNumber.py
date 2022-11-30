from random import randint
guessnumber=randint(1, 100)
attempts=0
guess=None
print("You have to guess the number which I'm thinking between 1 and 100.Good Luck!")
while guess!=guessnumber:
    try:
        attempts+=1
        guess=int(input("Enter your guess:"))
        if guess<guessnumber:
            print("Your guess is lower")
        elif guess>guessnumber:
            print("Your guess is higher")
        else:
            break
    except ValueError:
        print("Your guess must be a number fool")
print("Congratulations! You guessed the number correctly. It took you {} attempts".format(attempts))
