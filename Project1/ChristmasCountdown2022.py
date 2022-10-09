import datetime
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

dt = datetime.datetime
today = dt.now()

daysUntil = dt(year = 2022, month = 12, day = 25) - dt(year = today.year, month = today.month, day = today.day)

favMovie = input("Christmas 2022 is approaching! Enter your favorite Christmas Movie to see how many days until Christmas. Hit enter when you are finished. ")
print ((favMovie) + " is a good one!! My favorite is The Elf! Now.. the countdown begins!")



print (colors.RED + "CHRISTMAS" + colors.RESET + colors.GREEN + " COUNTDOWN" + colors.RESET + colors.RED + " 2" + colors.RESET + colors.GREEN + "0" + colors.RESET + colors.RED + "2" + colors.RESET + colors.GREEN + "2" + colors.RESET + colors.RED + "!" + colors.RESET)
print ("There are " + colors.GREEN + str(daysUntil.days) + colors.RESET + " days until" + colors.RED + " Santa" + colors.RESET + " comes!")


## https://pythonicpi.wordpress.com/2017/12/04/christmas-countdown-with-python/
