import pandas as pd
import os
import art
#from wiper import wipe
clear = lambda: os.system('cls')


def main_menu():
    print(text2art("Saving Goal"))
    print("1. Creat a New Saving Goal")
    print("2. Adding money to Saving Goal")
    print("3. View and Edit Exsiting Saving Goals")
    print("4. View Achieved Saving Goals")
    print("5. Exit")
    input = int(input("Please enter the number:"))
    try:
        if input == 1:
            create_goal()
        elif input == 2:
            add_money()
        elif input == 3:
            view_goal()
        elif input == 4:
            view_achieved()
        elif input == 5:
            exit()
    except ValueError:
        print("Please enter a valid number")







