#title: bank balance/budget analysis
#author: michael stoll
#date: 2/5/25
bank_balance = int(input('Enter bank balance:'))
budgets = int(input('Enter amount of budgets:'))
budget_list = []
for count in range(1, budgets + 1):
    budget_list += [int(input('Enter amount budgeted:'))]
total_budget = sum(budget_list)
bank_balance = bank_balance-total_budget
print("New bank balance:", bank_balance)
if bank_balance < 0:
    print('Bank overdrawn.')