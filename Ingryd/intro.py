print('I am a boy')

# Data types
'''
1. Numbers - (floats & integers)
2. Strings
3. Boolean
4. None type
5. Complex
'''

x = 5
print(x, type(x))
x = 6.7
print(x, type(x))
x = 'Hello world!'
print(x, type(x))
x = True
print(x, type(x))
x = None
print(x, type(x))
x = 5 + 3j
print(x, type(x))

'''
You have a budget of #20000 to spend at a store.
Write a program that asks the user for the price 
of an item, checks if they can afford it and 
tells them the balance left.
'''

# solution 
'''
 1 - declare a variable
 2 - accept input from the user
 3 - when input is less than or equal to than variable
 4 - print affordable
 5 - subtract input from variable to get balance
 6 - print balance
'''
budget = 20000
price = int(input('Enter the price of the item: '))

if price <= budget:
    print('You can afford this item')
    balance = budget - price
    print('Your balance is', balance)