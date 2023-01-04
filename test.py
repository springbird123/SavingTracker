import pandas as pd
df = pd.read_csv('saving_goal.csv')
index = input("Please enter the index on the left side of the saving goal that you want to add the money: ")
add = input("Please enter the amount you want to add:")
current_amount = df.loc[int(index), ['Current_amount']]
df.loc[int(index), ['Current_amount']] = current_amount + float(add)
print(current_amount)
print(df)
df.to_csv('./saving_goal.csv', index=False)