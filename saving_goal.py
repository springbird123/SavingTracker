import pandas as pd

goal_name = []
current_amount = []
goal_amount = []
saving_goal = {'goal_name': goal_name, 'current_amount': current_amount, 'goal_amount': goal_amount,}
saving_goals = pd.DataFrame(saving_goal)

saving_goals.to_csv('./a.csv')
