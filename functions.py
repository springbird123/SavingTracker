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

