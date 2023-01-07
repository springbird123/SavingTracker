import pandas as pd
import os
from art import *
import datetime
import time

clear = lambda: os.system('clear')
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
            print('----------main menu----------')
            print('')
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
            # Exit    
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
    print('---------- Create New Goal ----------')
    goal_name = input("Please enter the goal name: ")
    while True:
        # check if the amount input is a valid number
        try: 
            amount = input("Please enter the amount you want to save: ")
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        # error handling in case a non-float is inputted  
        except ValueError:
            print("Please enter a valid amount")
    goal_list = [goal_name, 0, amount, '0%']
    # read the csv file
    df = pd.read_csv('saving_goal.csv')  
    #save the goal to the csv file
    df.loc[len(df)] = goal_list
    df.to_csv('saving_goal.csv', index=False)
    print("Your new saving goal has been created!")
    input("Please Press Enter to back to menu:")
    main_menu()

#display the ongoing saving goals
def view_goal():  
    clear()
    #read csv file
    df = pd.read_csv('saving_goal.csv')
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

# function for adding money to a saving goal
def add_money():
    #display the ongoing saving goals
    view_goal()      
    # handle the error if input is not the index  #      
    try:
        df = pd.read_csv('saving_goal.csv')
        index = input("Please enter the index on left side of the saving goal name that you want to add money: ")
        df.loc[int(index)]
    except:
        input("Invalid index, please press enter to try again:")
        add_money()
    add = input("Please enter the money amount you want to add:")
    # handle the error if input is not a number
    try:
        add = float(add)
    except ValueError:
        print("Please enter a valid amount")
    # update the saving amount from the file
    df.loc[int(index), ['Current_amount']] = df.loc[int(index), ['Current_amount']] + float(add)
    # check process
    check_progress(df, index)
    print("Your new contribution has been added!")
    input("Please Press Enter to back to menu:")
    main_menu()

#function for editing an existing saving goal
def edit_goal():
    #display the ongoing saving goals
    view_goal()       
    # input the index  
    try:
        df = pd.read_csv('saving_goal.csv')
        index = input("Please enter the index of the saving goal that you want to edit: ")
        df.loc[int(index)]
    except:
        input("Invalid index, please press enter to try again:")
        add_money()
    #display edit menu  
    print('')   
    print('----------editing menu----------')
    print('')
    print('Edit 1. Edit the goal name')
    print('Edit 2. Edit the goal amount')
    print('Edit 3. Delete the selected goal')
    print('Edit 4. Reselect the goal')
    print('Edit 5. Return to the main menu')    
    print('')    
    while True:
        # check if the amount input is a valid number 
        try:        
            ipt = int(input('Please enter the edit number(1-5): Edit '))
            # edit the goal name
            if ipt == 1:
                print('----------edit the goal name----------')
                new_name = input("Please enter the new goal name: ")
                df.loc[int(index), ['Goal_name']] = new_name
                df.to_csv('./saving_goal.csv', index=False)
                view_goal()
                input('You successfully changed the goal name, please press enter to return to the main menu')
                main_menu()
            #edit the goal amount
            elif ipt == 2:
                print('----------edit the goal amount----------')
                new_amount = input("Please enter the new goal amount: ")
                df.loc[int(index), ['Goal_amount']] = new_amount  
                # method check process 
                check_progress(df, index)
                input('You successfully updated the goal amount, please press enter to return to the main menu')
                main_menu()
            # delete the goal
            elif ipt == 3:   
                df.drop([int(index), ], inplace=True)    
                df.to_csv('./saving_goal.csv', index=False)  
                view_goal()      
                input('You successfully deleted the selected goal, please press enter to return to the main menu:')
                main_menu() 
            # reselect the goal    
            elif ipt == 4:
                edit_goal()   
            # return to the main menu      
            elif ipt == 5:
                main_menu()
            else:
                input("Invalid input, please try again:")
        except ValueError:
            input("Invalid amount, please again:")

def check_progress(df, index):
    current_amount = float(df.loc[int(index), ['Current_amount']])
    goal_amount = float(df.loc[int(index), ['Goal_amount']])
    # error handling to prevent amount below 0
    if current_amount <0 or goal_amount <= 0:
        print('current/goal amount can not be below 0, please try again.' )
        input('Please press enter to return the main menu:')
        main_menu()
    # congratulation page with updated data when goal is reached  
    elif current_amount >= goal_amount:
        clear()
        # ASCII text from art package
        tprint("100%! Congratulations!") 
        Goal_name = str(df.loc[int(index), ['Goal_name']])
        print('Congratulations! You have successfully reached your saving goal!')
        # updating the saving process
        df.loc[int(index), ['Process']] = "Completed!"
        df.to_csv('./saving_goal.csv', index=False)
        input('Now you can return to menu to see your achieved goals:') 
        main_menu()              
    else:
        # updating the saving process with '%' form
        df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
        # save the update in the file
        df.to_csv('./saving_goal.csv', index=False)
        # display the updated amount and process
        view_goal() 

main_menu()