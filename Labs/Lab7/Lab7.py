# my module I chose for this lab
import math

# asking user how many digits of pi they know
answer1 = input("How many digits of Pi do you know? Type what you think Pi is ")

# printing their answer and the correct answer
    print ("Close!! Your guess was " + answer1)
    print ("it is actually " + str(math.pi))
    
# asking user for their guess on the cosine of Pi
answer2 = input("Since we are talking about Pi, lets find the cosine of it. Any guesses? ")

# function to solve the cosine of pi, and printing it to the user
answer3 = math.cos(3.141592653589793)
    print ("The cosine of Pi is " + str(answer3))

answer4 = input("For our last function, lets find the square root of Pi. Any guesses? A hint: Not what you think! ")

# showing the user the square root of Pi 
answer5 = math.sqrt(math.pi)
    print ("The square root of Pi is " + str(answer5))
    print ("Thanks for checking out my script!")
