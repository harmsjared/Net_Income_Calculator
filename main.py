items = ['Bubblegum', 'Toffee', 'Ice Cream',
         'Milk Chocolate', 'Doughnut', 'Pancake']
costs = [2, 0.2, 5, 4, 2.5, 3.2]
amounts = [101, 590, 450, 420, 430, 25]
item_totals = []

for c, a in zip(costs, amounts):
    item_totals.append(c * a)

print('Earned amount:')
for i, c, a in zip(items, costs, amounts):
    print(str(i) + ': $' + str(int(c * a)))

income = sum(item_totals)
print()
print('Income: $' + str(int(income)))

staff_expenses = str(input("Staff expenses: "))
print('> ' + staff_expenses)
other_expenses = str(input("Other expenses: "))
print('> ' + other_expenses)
net_income = income - int(staff_expenses) - int(other_expenses)
print('Net income: $' + str(int(net_income)))
