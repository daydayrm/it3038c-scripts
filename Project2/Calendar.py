
import calendar

# Welcome Statement, Preparing the user for input
print("Welcome to my Calendar Script! You choose a month and year and we will display it in calendar form.")

# Taking user input here, this will determine the output
year = int(input("Please enter a year: "))
month = int(input("Please enter the month in number form: "))

# Printing the selected Calendar for the user
print(calendar.month(year, month))

# Second function I am using. This will calculate if the year is a leap year or not. The year will be stored by user input
print("The last function of my script is a leap year determiner. With the input of a year, the script will determine if it was a leap year or will be a leap year.")

# User input, year to determine leap year
leapYear = int(input("Please enter a year: "))

# Displaying True or False, True for leap year and false if not
print(calendar.isleap(leapYear))
           
