# pcost.py
#
# Exercise 1.27

with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    total_cost = 0
    for line in f:
        row = line.split(',')
        cost = int(row[1]) * float(row[2])
        total_cost += cost
    print(f'{total_cost:.2f}')
