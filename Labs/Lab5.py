import random
number = random.randint(1, 30)

guesses = 0
print("Can you guess the random number between 1 and 30?")

while guesses < 5:
    guess = int(input())
    guesses += 1
    if guess > number: 
        print("Too high! Guess lower.")
    if guess < number:
        print("Too low! Guess higher.")
    if guess == number:
        break
        
        
if guess == number: 
    print("CORRECT! You guessed the number in " + str(guesses) + " attempts! ")
else:
    print("Not very good guesses. The number was " + str(number)) 
