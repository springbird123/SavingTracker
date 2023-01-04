import pandas as pd
import os
from art import *
import datetime
import time
import random
clear = lambda: os.system('cls')
logo = text2art("Saving Goal")

# clear the screen with logo and welcome message
def welcome():
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
    while (1):
        try: # error handling in case a non-integer is inputted
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
                clear()
                print("Thank you! See you next time!")
                exit()
            else:
                print("Invalid Input, please enter a valid number:")
        except ValueError:
            print("Invalid Input, please enter a valid number:")

# function for creating a new goal
def create_goal():    
    goal_name = input("Please enter the goal name: ")
    print()
    while (1):
        try: # check if the amount input is a valid number
            amount = input("Please enter the amount you want to save: ")
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid amount")
    goal_list = [goal_name, 0, amount, '0%']
    #save the goal to the csv file
    df = pd.read_csv('saving_goal.csv')
    df.loc[len(df)] = goal_list
    df.to_csv('saving_goal.csv', index=False)
    print("Your new saving goal has been created!")
    input("Please Press Enter to back to menu:")
    main_menu()

#display the ongoing saving goals
def view_goal():
    clear()
    print(logo)
    df = pd.read_csv('saving_goal.csv')
    print(df)
    print("")


def add_money():
    #display the ongoing saving goals
    view_goal()
    # read csv file
    df = pd.read_csv('saving_goal.csv')
    while True:
        index = input("Please enter the index on the left side of the saving goal that you want to add the money: ")
        try:
            index = int(index)
            break
        except ValueError:
            print("Please enter a valid index")
        for i in df.index:
            if i == index:
                    break
            else:
                print("Please enter a valid index")
        add = input("Please enter the amount you want to add:")
        try:
            add = float(add)
            break
        except ValueError:
            print("Please enter a valid amount")
    # update the saving amount from the file
    df.loc[int(index), ['Current_amount']] = df.loc[int(index), ['Current_amount']] + float(add)
    current_amount = float(df.loc[index, ['Current_amount']])
    # updating the saving process with '%' form
    goal_amount = df.loc[int(index), ['Goal_amount']]
    df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
    # save the update in the file
    df.to_csv('./saving_goal.csv', index=False)
    # display the updated amount
    view_goal() 
    print("Your new contribution has been added!")
    input("Please Press Enter to back to menu:")
    main_menu()


#function for editing an existing saving goal
def edit_goal():
    clear()


#function for viewing the achieved saving goals
def view_achieved():
    clear()

main_menu()

