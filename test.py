import pandas as pd


#display the ongoing saving goals
# read csv file
df = pd.read_csv('saving_goal.csv')
print(pd)
# handle the error if input is not the index
#input_index('add money')      
index = input("Please enter the index on the left side of the saving goal that you want to add money:")
try:
    df.loc[int(index)]
except:
    input("Invalid index, please try again.")
# handle the error if input is not a number
add = input("Please enter the money amount you want to add:")
try:
    add = float(add)
except ValueError:
    input("Invalid input, please try again.")
# update the saving amount from the file
df.loc[int(index), ['Current_amount']] = df.loc[int(index), ['Current_amount']] + float(add)
current_amount = float(df.loc[int(index), ['Current_amount']])
# check if the goal is accomplished
goal_amount = df.loc[int(index), ['Goal_amount']]
if current_amount >= goal_amount:
    clear()
    text2art("Congratulations! ")
    print('Congratulations! You have successfully reached your saving goal!')
    print('Now you can return to menu to see your achieved goals')              
else:
    # updating the saving process with '%' form
    df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
    # save the update in the file
    df.to_csv('./saving_goal.csv', index=False)
    # display the updated amount and process
    view_goal() 
    print("Your new contribution has been added!")
input("Please Press Enter to back to menu:")
