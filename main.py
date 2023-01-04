import pandas as pd
import os
from art import *
import menu
clear = lambda: os.system('cls')

def welcome():
    logo = text2art("Saving Goal")
    clear()
    print(logo)
    print("Welcome to the Saving Goal!")
    print("")




def main_menu():
    welcome()
    print("1. Creat a New Saving Goal")
    print("2. Adding money to Saving Goal")
    print("3. View and Edit Exsiting Saving Goals")
    print("4. View Achieved Saving Goals")
    print("5. Exit")
    try:
        ipt = int(input("Please enter the number:"))
        if ipt == 1:
            create_goal()
        elif ipt == 2:
            add_money()
        elif ipt == 3:
            view_goal()
        elif ipt == 4:
            view_achieved()
        elif ipt == 5:
            print("See you next time!")
            exit()
    except ValueError:
        print("Please enter a valid number:")


main_menu()
