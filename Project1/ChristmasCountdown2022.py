## Project 1 - Christmas Countdown 2022

import datetime
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
# Christmas Colors for the Countdown display! Instead of using modules I just used ANSI color codes and stored them as variables to make it easier. 

dt = datetime.datetime
today = dt.now()

# Variables for the dates. It includes the day we are looking for (Christmas), minus the current date.

daysUntil = dt(year = 2022, month = 12, day = 25) - dt(year = today.year, month = today.month, day = today.day)

# Performs the calculation of the countdown

favMovie = input("Christmas 2022 is approaching! Enter your favorite Christmas Movie to see how many days until Christmas. Hit enter when you are finished. ")
print ((favMovie) + " is a good one!! My favorite is The Elf! Now.. the countdown begins!")

# A simple prompt asking for the user's favorite Christmas Movie. The Countdown only works after the user has provided input. The system will respond with a statement about their selected movie.

print (colors.RED + "CHRISTMAS" + colors.RESET + colors.GREEN + " COUNTDOWN" + colors.RESET + colors.RED + " 2" + colors.RESET + colors.GREEN + "0" + colors.RESET + colors.RED + "2" + colors.RESET + colors.GREEN + "2" + colors.RESET + colors.RED + "!" + colors.RESET)
print ("There are " + colors.GREEN + str(daysUntil.days) + colors.RESET + " days until" + colors.RED + " Santa" + colors.RESET + " comes!")

# Printing to the user the Christmas Countdown Calculator and how many days until Santa comes. It will be shown in different colors to match the Christmas Theme.
# End of Project1


## https://pythonicpi.wordpress.com/2017/12/04/christmas-countdown-with-python/
## For the idea of this project, I visited the above link. I have added lots of details and changed a lot of details. Different variable names, additional features, colored font, and more responsive.
