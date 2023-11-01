'''
Write a program that convert a temperature in celcius to fahrenheit.
The program should prompt the user for the temperature value.
'''

# Solution:

# Code (mtd 1):
# celcius = float(input("Enter a temperature in celcius: "))
# fahrenheit = (celcius * 9/5) + 32
# print("Temperature in fahrenheit is: ", fahrenheit)

# # mtd 2
# celcius = float(input("Enter a temperature in celcius: "))
# fahrenheit = (celcius * 1.8) + 32
# print("Temperature in fahrenheit is: ", fahrenheit)

z = input('Enter a number: ')
y = input('Enter another number: ')
x = z + y
print(x)

# Strings
name = 'John Doe'
#print(name)
school = "Moringa School"
#print(school)
club = '''Moringa School's Club'''
#print(club)

# String Concatenation
first_name = 'John'
last_name = 'Doe'

full_name = first_name + ' ' + last_name
print(full_name)

# # Strings are arrays
# # Accessing characters in a string
# print(full_name[5])

# # Slicing
# print(full_name[2:5])

# x = full_name[:5]
# print(x, 'size is =>', len(x))

# y = full_name[:4]
# print(y, 'size is =>',len(y))

# print(full_name[2:])

# # Negative Indexing
# print('-ve indexing =>',full_name[-4:-1]) # space Do
# print('+ve indexing =>',full_name[4:1]) # this is wrong according to number line system
# print('+ve indexing =>',full_name[1:4]) # this is right according to number line system

# print(full_name[-7:-3])
# answer: ohn 

# a = full_name[-6]
# print(a)
# x = full_name[:-6]
# y = full_name[:-6:-2]
# print(x, len(x))
# print(y, len(y))

# school = 'ingryd academy' # space acade
# a = school[-8:-2]
# print('a => ',a, len(a))
# b = school[-2:-8:-3] 
# print('b => ',b, len(b))
# c = school[-8:-2:3]
# print('c => ', c, len(c))
# d = school[::-1]
# print('d => ',d, len(d))

# String Methods
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.title())
print(full_name.swapcase())

print()
# Check if a string is in upper case
print(full_name.isupper())
print(full_name.islower())
print(full_name.istitle())
print(full_name.isalpha()) 
print(full_name.isdigit())
print(full_name.isalnum())
print(full_name.isspace())
print(full_name.startswith('J'))
print(full_name.endswith('E'))
print(full_name.find('oe'))
print(full_name.count('o'))


# Substring search
print('this is the substring search: ', full_name.index('Doe'))
sentence = 'I love programming'
sentence2 = 'This is ingryd, academy. We\'re learning, python programming.'
key = 'prog'
print('key is found in index: ', sentence.find(key))

# string split method
c = sentence2.split()
print('this is the efault split without delimeter: ',c)
print(c[3])

# split with a delimiter
print('this is the split with delimeter: ', sentence2.split(','))

# sting replace method
print(sentence2.replace('ingryd', 'Moringa'))

# Palindrome task
# what is a palindrome? 
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, 
# such as madam, racecar, lawal.

# solution

'''
1. accept word from user
2. convert it to lower case, reverse the word and remove spaces
3. compare the word and the reversed word
4. if they are the same, then it is a palindrome
5. else, it is not a palindrome
6. print the result
'''
# mtd 1:
word = input('Enter a word: ')

# convert to lower case
word = word.upper()
print('word is now lowered: ', word)

# reverse the word
reversed_word = word[::-1]
print('reversed word is: ', reversed_word)

# remove spaces
word = word.replace(' ', '')
print('word is now spaceless: ', word)

# compare the word and the reversed word
if word == reversed_word:
    print('The word is a palindrome')
else:
    print('The word is not a palindrome')

#print('noon' == 'Noon')

# mtd 2: 
word = input('Enter a word: ') # ask user for word
word = word.lower().replace(' ', '') # convert to lower case and remove spaces
print('converted word: ', word)
is_palindrome = word == word[::-1] # compare the word and the reversed word
print(is_palindrome)
print('The word is a palindrome => ', is_palindrome) if is_palindrome else print('The word  \
                                                        is not a palindrome => ', is_palindrome)

# sring formatting


# give an introductory class on functions
# functions
# what is a function?
# a function is a block of code that performs a specific task
# it is also called a method
# it is also called a procedure
# it is also called a subroutine
# it is also called a subprogram

# why do we use functions?
# to avoid repetition of code
# to improve code readability
# to improve code maintainability
# to improve code reusability
# to improve code testability
# to improve code efficiency

# how do we create a function?
# syntax:
# def function_name():
#     function body
#     function body
#     function body
#     function body

# how do we call a function?
# syntax:
# function_name()

# example:
# def say_hello():
#     print('Hello World')

# say_hello()

# def say_hello():
#     print('Hello World')

# say_hello()

# functions with parameters
# def say_hello(name):
#     print('Hello', name)

# say_hello('John')
# say_hello('Jane')

# functions with default parameters
# def say_hello(name='John'):
#     print('Hello', name)

# say_hello()
# say_hello('Jane')

# functions with return values
# def say_hello(name='John'):
#     return 'Hello ' + name

# print(say_hello())
# print(say_hello('Jane'))

# functions with multiple parameters
# def say_hello(first_name, last_name):
#     return 'Hello ' + first_name + ' ' + last_name

# print(say_hello('John', 'Doe'))

# functions with keyword arguments
# def say_hello(first_name, last_name):
#     return 'Hello ' + first_name + ' ' + last_name

# print(say_hello(last_name='Doe', first_name='John'))

# functions with arbitrary arguments
# def say_hello(*names):
#     for name in names:
#         print('Hello', name)

# say_hello('John', 'Jane', 'Doe', 'Mary')  

# functions with arbitrary keyword arguments
# def say_hello(**names):
#     for key, value in names.items():
#         print('Hello', key, value)

# say_hello(first_name='John', last_name='Doe', middle_name='Jane', maiden_name='Mary')

# functions with arbitrary keyword arguments
# def say_hello(**names):
#     for key, value in names.items():
#         print('Hello', key, value)

# say_hello(first_name='John', last_name='Doe', middle_name='Jane', maiden_name='Mary')

# functions 


