from random import randint
guessnumber=randint(1, 100)
attempts=0
guess=None
print("You have to guess the number which I'm thinking between 1 and 100.Good Luck!")
while guess!=guessnumber:
    try:
        guess=int(input("Enter your guess:"))
        if guess<guessnumber:
            print("Guess is too low. Enter a higher number")
            attempts+=1
        elif guess>guessnumber:
            print("Guess is too high. Enter a lower number")
            attempts+=1
        else:
            break
    except ValueError:
        print("Invalid Input. Please enter a number")
        continue
print("Congratulations! You guessed the number correctly. It took you {} attempts".format(attempts))