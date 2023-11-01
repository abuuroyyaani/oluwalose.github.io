# Python fundamentals

a = -200
print(a, type(a))
a = 'Nigeria is cool'
print(a, type(a))
a = 789.67
print(a, type(a))
a = False
print(a, type(a))
a = 4 + 3j
print(a, type(a))
a = None
print(a, type(a))

# Operators
x = 45/9
y = 5 * 3
z = x == y

print(z, type(z))


'''
You have a budget of #20000 to spend at a store.
Write a program that asks the user for the price 
of an item, checks if they can afford it and 
tells them the balance left.
'''      

budget = 20000
item_price = int(input('Enter the price of the item: '))
if budget >= item_price:
    balance = budget - item_price
    print('Your balance is #',balance)
    print('You can afford the item. Thanks!')

