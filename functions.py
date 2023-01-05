import pandas as pd

def input_index(x):
    df = pd.read_csv('saving_goal.csv')
    # handle the error if input is not the index
    while True:        
        index = input(f"Please enter the index on the left side of the saving goal that you want to {x} ")
        try:
            df.loc[int(index)]
        except:
            print("Invalid index, please try again.")
        else:
            return index, df

def check_progress():
    current_amount = float(df.loc[int(index), ['Current_amount']])
    goal_amount = float(df.loc[int(index), ['Goal_amount']])
    # error handling to prevent amount below 0
    if current_amount <=0 or goal_amount < 0:
        print('current/goal amount can not below 0, please try again' )
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
        input('Now you can return to menu to see your achieved goals:') 
        main_menu()              
    else:
        # updating the saving process with '%' form
        df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
        # save the update in the file
        df.to_csv('./saving_goal.csv', index=False)
        # display the updated amount and process
        view_goal() 