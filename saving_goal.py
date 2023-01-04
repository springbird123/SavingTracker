import pandas as pd

def percentage(x, y):
    return ('%.2f%%' % (x / y * 100))

df = pd.read_csv('saving_goal.csv')
index = input("Please enter the index on the left side of the saving goal that you want to add the money: ")
add = input("Please enter the amount you want to add:")
current_amount = df.loc[int(index), ['Current_amount']]
df.loc[int(index), ['Current_amount']] = current_amount + float(add)
goal_amount = df.loc[int(index), ['Goal_amount']]
print(type(goal_amount.astype(float)))
#df.loc[int(index), ['Process']] = '%.2f%%' % (current_amount / goal_amount * 100)
print(df)
df.to_csv('./saving_goal.csv', index=False)