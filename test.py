import pandas as pd
df = pd.read_csv('saving_goal.csv')
index = input("Please enter the index on the left side of the saving goal that you want to add the money: ")
add = input("Please enter the amount you want to add:")
df.loc[int(index), ['Current_amount']] = df.loc[int(index), ['Current_amount']] + float(add)
current_amount = float(df.loc[int(index), ['Current_amount']])
goal_amount = df.loc[int(index), ['Goal_amount']]
df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
print(df)

