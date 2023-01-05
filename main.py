import pandas as pd
import os
from art import *
import datetime
import time
from functions import *
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
    while True:    
        try: 
            print("1. Creat a New Saving Goal")
            print("2. Adding money to Saving Goal")
            print("3. View and Edit all Saving Goals")
            print("4. Exit")
            ipt = int(input("Please enter the number:"))
            if ipt == 1:
                create_goal()
            elif ipt == 2:
                add_money()
                break
            elif ipt == 3:
                edit_goal()
            elif ipt == 4:
                clear()
                print("Thank you! See you next time!")
                exit()
            else:
                print("Invalid Input, please enter a valid number:")
        # error handling in case a non-integer is inputted        
        except ValueError:
            input("Invalid Input, please press enter to the main menu to try again:")
            main_menu()

# function for creating a new goal
def create_goal():    
    goal_name = input("Please enter the goal name: ")
    while True:
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
    df = pd.read_csv('saving_goal.csv')    
    clear()
    # handle the error if saving goal list is empty      
    try: 
        df.loc[0]
    except:
        clear()
        tprint("EMPTY.....")
        input('There is no saving goal yet, return to the main menu to create a new one!')
        main_menu()  
    print(logo)
    print(df)
    print("")


def add_money():
    # read csv file
    df = pd.read_csv('saving_goal.csv')
    #display the ongoing saving goals
    view_goal()      
    # handle the error if input is not the index     
    try:
        index = input("Please enter the index of the saving goal that you want to add money: ")
        df.loc[int(index)]
    except:
        input("Invalid index, please press enter to try again:")
        add_money()
    # handle the error if input is not a number
    add = input("Please enter the money amount you want to add:")
    try:
        add = float(add)
    except ValueError:
        print("Please enter a valid amount")
    # update the saving amount from the file
    df.loc[int(index), ['Current_amount']] = df.loc[int(index), ['Current_amount']] + float(add)
    current_amount = float(df.loc[int(index), ['Current_amount']])
    # check if the goal is accomplished
    goal_amount = float(df.loc[int(index), ['Goal_amount']])
    if current_amount >= goal_amount:
        clear()
        tprint("100%! Congratulations!")
        Goal_name = str(df.loc[int(index), ['Goal_name']])
        print('Congratulations! You have successfully reached your saving goal!')
        input('Now you can return to menu to see your achieved goals:')
        main_menu()                  
    else:
        # updating the saving process with '%' form
        df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
        # save the update in the file
        df.to_csv('./saving_goal.csv', index=False)
        # display the updated amount and process
        view_goal() 
        print("Your new contribution has been added!")
        input("Please Press Enter to back to menu:")
        main_menu()


#function for editing an existing saving goal
def edit_goal():
    # read csv file
    df = pd.read_csv('saving_goal.csv')
    #display the ongoing saving goals
    view_goal()       
    #display edit menu  
    print('')   
    print('Edit 1. Edit the goal name')
    print('Edit 2. Edit the goal amount')
    print('Edit 3. Delete the selected goal')
    print('Edit 4. Reselect the goal')
    print('Edit 5. Return to the main menu')    
    print('')    
    # handle the error if input is not the index     
    try:
        index = input("Please enter the index of the saving goal that you want to add money: ")
        df.loc[int(index)]
    except:
        input("Invalid index, please press enter to try again:")
        add_money()
    while True:
        # check if the amount input is a valid number 
        try:        
            ipt = int(input('Please enter the edit number(1-5): Edit '))
            if ipt == 1:
                new_name = input("Please enter the new goal name: ")
                df.loc[int(index), ['Goal_name']] = new_name
                df.to_csv('./saving_goal.csv', index=False)
                view_goal()
                input('You successfully changed the goal name, please press enter to return to the main menu')
                main_menu()
            elif ipt == 2:
                new_amount = input("Please enter the new goal amount: ")
                df.loc[int(index), ['Goal_amount']] = new_amount
                df.to_csv('./saving_goal.csv', index=False)
                view_goal()      
                input('You successfully updated the goal amount, please press enter to return to the main menu')
                main_menu()
            elif ipt == 3:   
                df.drop([int(index), ], inplace=True)    
                df.to_csv('./saving_goal.csv', index=False)  
                view_goal()      
                input('You successfully deleted the selected goal, please press enter to return to the main menu')
                main_menu() 
            elif ipt == 4:
                edit_goal()   
            elif ipt == 5:
                main_menu()
            else:
                input("Invalid input, please press enter to try again:")
        except ValueError:
            input("Invalid amount, please press enter to try again:")

    
#function for viewing the achieved saving goals
def view_achieved():
    clear()
    input("Please Press Enter to back to menu:")
    main_menu()

main_menu()