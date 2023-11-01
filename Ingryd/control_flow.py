# String formatting

# name = 'John'
# age = 20

# # string concatenation
# print('Hello ' + name + ' you are ' + str(age) + ' years old')

# # string interpolation
# print('Hello {} you are {} years old'.format(name, age))

# # string interpolation with index
# print('Hello {1} you are {0} years old'.format(age, name))

# # string interpolation with keyword arguments
# print('Hello {name} you are {age} years old'.format(name='James', age=25))

# # f-strings method
# print(f'Hello {name} you are {age} years old')

# 2 decimal place example
pi = 3.14159265
print('Pi is', round(pi, 2)) # using round function
# using string format to make it 2 dp
print('Pi is {:.2f}'.format(pi))

'''
1. You're developing a report generator. You have data about sales, including the
product name, quantity sold, and total sales amount. Create a program that 
takes this data and generate a report in the following format:

Product: <product name>
Quantity: <quantity sold>
Total Sales: #<total sales amount> to 2 dp.

2. You're building a program to generate a personalized email msg. The user 
provides their name and age. Write a program that takes these input and create 
an email msg in the following format:  

Hello  <name>, you are <age> years old.
'''

# code 
# report generator
# product_name = input('Enter product name: ')
# quantity_sold = int(input('Enter quantity sold: '))
# total_sales = float(input('Enter total sales: '))
# report = f"Product: {product_name}\nQuantity: {quantity_sold}\nTotal Sales: \
# #{total_sales:.2f}"
# print(report)

# print(f'Product: {product_name}')
# print(f'Quantity: {quantity_sold}')
# print(f'Total Sales: #{total_sales:.2f}')

# personalized email msg
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# email_msg = 'Hello {}, you are {} years old.'.format(name,age)
# print(email_msg)

# another string format task
"""
You're building a URL generator. The user provides a domain name and a path.
Write a program that takes these inputs and create a complete URL. Ensure the 
URL includes "https://" at the beginning. 
"""


# Control flow statements
# if statement
# syntax:
# if condition:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult.\nYou can vote')
#     #print('You can vote')

# if-else statement
# syntax:
# if condition:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# else:
#     print('You are not an adult')
#     print('You cannot vote')

# if-elif-else statement
# syntax:
# if condition:
#     code block
#     code block
# elif condition:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# elif age >= 13:
#     print('You are a teenager')
#     print('You cannot vote')
# else:
#     print('You are a child')
#     print('You cannot vote')

#coach = input('Enter your coach: ').lower()
#coach = coach.lower()
# if coach == 'pep':
#     print('Man city will win the league.\nThey\'ll win the ucl.')
# elif coach == 'ancelotti':
#     print('Madrid will win the league.\nThey will win the ucl.')
# elif coach == 'inzaghi':
#     print('Inter will win the league.\nThey will win the ucl.')
# else:
#     print('I don\'t know who will win the league.')


#game = input('Enter your fav game: ').capitalize()

# if game == 'Monopoly':
#     print('Hikmat will win')
# elif game == 'Squid':
#     print('Omowunmi will win')
# elif game == 'Ludo':
#     print('Oluwaferanmi will win')
# else:
#     print('I don\'t know who will win') 


# nested if statement
# syntax:
# if condition:
#     code block
#     code block
#     if condition:
#         code block
#         code block
#     else:
#         code block
#         code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
#     if age >= 21:
#         print('You can drive')
#     else:
#         print('You cannot drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     if age >= 13:
#         print('You can play fortnite')
#     else:
#         print('You cannot play fortnite')

'''
1. You're building a grade calculator program. The user provides their test 
score (btw 0 - 100), and you need to determine their grade based on the ffg
criteria:
A: 70 - 100
B: 60 - 69
C: 50 - 59
D: 40 - 49
E: 30 - 39
F: 0 - 29

2. You're building a program to determine the cost of a trip. The user provides
the distance of the trip in miles, and you need to determine the cost of the
trip based on the ffg criteria:
Distance <= 100 miles: $5
Distance > 100 miles and <= 500 miles: $8
Distance > 500 miles: $10

3. You're developing a program for a movie theater to calculate ticket prices.
The user enters their age and the movie time (morning, afternoon or evening). 
The ticket prices are as follows:
- Morning shows are #100 for all ages.
- Afternoon shows are #150 for adults (18 and above) and #100 for children.
- Evening shows are #200 for adults and #100 for children.
Write a program to calculate and display the ticket price. 
'''

# code
test_score = int(input('Enter your test score: '))

if test_score > 100:
    print('Not applicable. Stop lying!')
elif test_score >= 70:
    print('Your grade is A')
elif test_score >= 60:
    print('Your grade is B')
elif test_score >= 50:
    print('Your grade is C')
elif test_score >= 40:
    print('Your grade is D')
elif test_score >= 30:
    print('Your grade is E')
else:
    print('Your grade is F')


# logical operators
# and, or, not

# example:
# age = int(input('Enter your age: '))
# if age >= 18 and age >= 21:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')

# example:
# age = int(input('Enter your age: '))
# if age >= 18 or age >= 21:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')

# example:
# age = int(input('Enter your age: '))
# if not age >= 18:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')
# else:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')

# for else
# syntax:
# for item in iterable:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# for i in range(5):
#     print(i)
# else:
#     print('Loop completed')

# while else


