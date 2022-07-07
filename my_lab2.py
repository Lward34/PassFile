"""The applicative prompts user to pick an option to do a math performance or secure functions"""
# Library import
import random
import math
from datetime import date

# library characters list
UP = "A B C D E F G H I J K L M N O P Q R S TU V W X Y Z"
LOW = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
NUM = "012456789"
SPEC = "`~!@#$%^&*()-_=+[{]};:',<.>?|]"
D = str()
i = 0


def display_menu():
    """The function prompts the user for input if they select
    a mathematical performance or generate a secure password.
    Otherwise, if the user selects category 3,
    there would be no input other than the menu selection.

    Args:None
    Returns:None
    """
    # show the options for the user to choose
    print("*********************************************")
    print("1: Generate Secure Password")
    print("2: Calculate and Format Percentage")
    print("3: How many Days from Today until July 4, 2025")
    print("4: Use the law of Cosine to calculate the leg of a triangle")
    print("5: Calculate the Volume of a Right Circular Cylinder")
    print("6: ""'EXIT' this program""")
    print("********************************************")
    print("Welcome to the lab Math and Secret Generation")


# run while tool until user do not quit
while True:
    display_menu()
    # Prompt user to take input  40
    select = int(input("Please enter your choice: "))
    # check if pick 1 is requested
    if select == 1:
        length = int(input("Enter password's length: "))
    # checks if the length is correct
    # if 'not' prints a message/restarts the while loop  40
        if length < 1:
            print("Invalid length; length must be above 1")
            continue
    # Prompts the user to get input and add
        print("Choose the characters you want in your password!")
        numb = int(input("To add Numbers enter 1 else enter 0:  "))
        upper = int(input("To add Upper letters enter 1 else enter 0: "))
        lower = int(input("To add Lower letters enter 1 else enter 0: "))
        symbols = int(input("To add Symbols enter 1 else enter 0:  "))
        PASSWORD = ""

    # checks the response and manages the options to add
        if numb == 1:
            D += NUM
        if upper == 1:
            D += UP
        if lower == 1:
            D += LOW
        if symbols == 1:
            D += SPEC
    # check and handled the inputs
        for i in range(0, length):
            # Picks random number based on the selection
            rand = random.randint(0, len(D) - 1)
            # Adds the corresponding characters
            PASSWORD += D[rand]
            # prints the secure password
            print("Secure Password is: ", PASSWORD + D)
    # prompts the user and gets selected choice
    elif select == 2:
        numerator = float(input("Enter the Numerator: "))
        denominator = float(input("Enter the Denominator: "))
        decimal = int(input("The number of decimal points for formatting: "))
        percentage = numerator / denominator * 100
        final = round(percentage, decimal)
        print("Percentage: ", final)
    # prompts the user and gets selected choice
    elif select == 3:
        start = date.today()
        end = date(2025, 7, 4)
        count = end - start
        print("From today until July 4, 2025, there are: ", count.days)
    # prompts the user and gets selected choice
    elif select == 4:
        a = int(input("Enter the length of side A: "))
        b = int(input("Enter the length of side B: "))
        angles = int(input("Enter the Angle: "))
        C = a * a + b * b - 2 * a * b * math.cos(math.pi / 180 * angles)
        square_root = math.sqrt(C)
        print("The leg of the triangle: ", square_root)
        # prompts the user and gets selected choice
    elif select == 5:
        radius = int(input("Enter the Circular radius: "))
        height = int(input("Enter the Cylinder Height: "))
        volume = radius * radius * height * math.pi
        print("The Cylinder Volume: ", volume)
        # check and handle the answer
    else:
        print("Thank you for visiting this Application!!!")
        print("Good Bye")
        break
