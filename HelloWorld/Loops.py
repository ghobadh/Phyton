from functools import total_ordering

for item in 'Python':
    print(item)

for item in ['Gavin', 'Gargamel', 'G-Man']:
    print(item)

for item in range(5, 10 , 2): # 2 steps
    print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total+=price
print (f'Total: {total}')