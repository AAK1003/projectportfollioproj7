import pandas as pd

expense_file = r"C:\Users\kirth\Downloads\expenses.csv"
expense_chart = pd.read_csv(expense_file)

def view_expense():
    global expense_chart
    if len(expense_chart) == 0:
        print('The list is empty, please add to the list before viewing.')
    else:
        print(expense_chart)

def add_expense():
    global expense_chart
    date = input('What is the date of the expense(input as eg: 12/7/2026 for December 7, 2026)? ')
    description = input('Please give a quick description of the expense(eg: bought apples from Kroger). ')
    category = input('What is the category of the expense(eg: grocery)? ')
    ammount = input('What is the ammount of the expense(eg: 12.00)? ')
    new_row = {'Date': date, 'Description': description, 'Category': category, 'Ammount': ammount}
    expense_chart.loc[len(expense_chart)] = new_row

while True:
    action = input('What would you like to do with your expense sheet: Add(add), View(view), or Save and Leave(sal)? ').lower()
    if action == 'add':
        add_expense()
    elif action == 'sal':
        expense_chart.to_csv(expense_file, index = False)
        break
    elif action == 'view':
        view_expense()
    else:
        print('Invalid response, please try again with the given actions.')