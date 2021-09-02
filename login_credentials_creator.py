import random
import string

#Ask for User's First name
first_name = input("Please enter user's first name: ")

#Ask for User's last name
last_name = input("Please enter user's last name: ")

#defining a function to create username using firstname and lastname
def username(fisrt_name, last_name):
    #Username will consist of first character of first name and complete last name
    user_name = first_name[0]+last_name
    return("User's LoginID is " + user_name)

print(username(first_name,last_name))

#defining function to generate a random password
def password():
    #storing lowercase, uppercase, number and symbols in respective variables
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    #storing 8 random charcaters consisting of 2 of each lowercase, uppercase, numbers, symbols
    password_unshuffled = random.sample(lowercase_letters,2)+random.sample(uppercase_letters,2)+random.sample(numbers,2)+random.sample(symbols,2)
    #randomly shuffling stored characters
    random.shuffle(password_unshuffled)
    #creating a string from list
    password = "".join(password_unshuffled)
    return "User's temporary password is: " + password
    
print(password())
