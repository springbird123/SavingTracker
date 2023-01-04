while (1):
    try:
        amount = input("Please enter the amount you want to save: ")
        amount = float(amount)
        continue
    except ValueError:
        print("Please enter a valid amount")