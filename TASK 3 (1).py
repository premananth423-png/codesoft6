import random
import string

print("----RANDOM PASSWORD GENERATOR----")

#User input
length = int(input("Enter password length : "))
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters)for i in range(length))

#output
print("Your Random password is ",password)
