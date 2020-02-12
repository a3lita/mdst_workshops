"""
MDST Workshop 1 - Python Basics Starter Code
"""
# Add any imports you need here:
import base64
import random

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    number = int(input('enter a number: '))
    if number % 2 == 0:
        print('even!')
    else:
        print('odd!')

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    while True:
        guess = input('guess the number: ')

        if guess == 'exit':
            break
        else:
            guess = int(guess)

        number = random.randrange(1,9)

        if guess > number:
            print('Too high')
        if guess < number:
            print('Too low')
        if guess == number:
            print('You got it!')

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    string = input('enter a string: ')

    reverse = string[::-1]

    if string == reverse:
        print('True')
    else:
        print('False')

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    with open(filename, "w") as f:
        f.write(base64.b64encode(username.encode()).decode() + "\n")
        f.write(base64.b64encode(password.encode()).decode() + "\n")

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    with open(filename, "r") as f:
        dec_user = base64.b64decode(f.readline().encode()).decode()
        dec_pass = base64.b64decode(f.readline().encode()).decode()

    print(dec_user)
    print(dec_pass)

    if password is not None:
        part4a(filename, dec_user, password)

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
