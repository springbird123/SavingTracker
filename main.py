import pandas as pd
import os
from art import *
import menu
import datetime
import time
import random
import saving_goal
clear = lambda: os.system('cls')

# function for displaying menu
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
            edit_goal()
        elif ipt == 4:
            view_achieved()
        elif ipt == 5:
            print("Thank you! See you next time!")
            exit()
    except ValueError:
        print("Please enter a valid number:")

def create_goal():
    goal_list = pd.read_csv()
    goal_name = input("Please enter the goal name: ")
    amount = input("Please enter the amount you want save: ")




    print("Your new saving goal has been created!")

saving_goals = {
    "Travel to Tibet": [0,3000]
}

def view_goal():
    clear()
    print(pd.read_csv('./saving_goal.csv'))

main_menu()
