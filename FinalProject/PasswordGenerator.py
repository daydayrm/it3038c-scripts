import string
import secrets

# These are the variables that hold numbers, letters, and characters. This is what the script will use to generate the password
numbers = string.digits
letters = string.ascii_letters
characters = string.punctuation

# The password will consist of all 3; numbers, letters, and characters
pswdIncludes = numbers + letters + characters

# I usually have very long passwords due to being a Cybersecurity Major. The recommended password is between 16-20 characters long and I usually stick around this amount.
# For this project, I offered it as an input instead of just being used by me. Some sites have constraints on password length so this option is nice.
pswdLength = int(input("Please enter the length of the password: "))

# 8 is the general number of characters for a password, if less than 8, the script will print a message. 
if pswdLength < 8:
    print("Please select more characters for a stronger password! Here is the password you asked for.")


# Now, the script generates the password that will meet the conditions set while including the password length input from the user
password = ""
for i in range(pswdLength):
  password += "".join(secrets.choice(pswdIncludes))
 
# The password is generated for the user
print(password)
print("Please write your password down (OLD SCHOOL MODE) on pen and paper to stay as safe as possible!")

# I know this is not the most complex script ever but to me it is extremely useful.
# I have many accounts to many sites and try very hard not to use the same passwords.
