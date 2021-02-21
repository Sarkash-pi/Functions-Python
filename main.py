# def greet():
#   return 'Hello Sarkash'

# print(greet())

# =============><=============

'''
Functions with parameters
'''

# def greet(name):
#   '''
#     Greets a person passed in as argument
#     name: a name of a person to greet
#     '''
#   return f'hello {name}, Good morning'

# print(greet('Sarkash'))
# print(greet('Tina'))
# print(greet('Sardar'))

# help(greet) #making comment and use help to know the function better


'''
Arbitrary parameters
'''

# def fruits(*names):
#     '''
#     Accepts unknown number of fruit names and prints each of them
#     *name: list of fruits
#     '''
#     # names are tuples
#     print(names)

# fruits('Orange', 'Banana', 'Apple', 'Grapes')

'''
Keyword parameters
# '''

# def greet(name, msg):
#   '''
#   This function greets a person with a given message 
#   name: person to greet
#   msg: message to greet person with
#   '''
#   return f'Hello {name}, {msg}'

# print(greet('Sarkash', 'Good morning!'))
# print(greet('Good morning!', 'Martina'))

#this are keyword which is useful to put them in order
# print(greet(name='Sarkash', msg='Good morning!'))

# print(greet(msg='Good morning!', name='Martina'))

'''
Arbitrary Keyword parameters
'''

# def person(**student):
#   # print(type(student))
#   # print(student)
#   for key in student:
#     print(student[key])
# # person(fname='Sarkash', lname='Talib')
# person(fname='Sarkash', lname='Talib', subject='Python')

'''
Default parameters values
'''
# # we add a value in default which is davic
# def greet(name='david'):
#   return f'Hello, {name}'

# print(greet())
# print(greet('Sana'))

''' 
Pass statement
'''

# def greet():
#   pass

'''
Recursion
'''

def factorial_recursive(n):
    '''
    Multiply a given number by every number less than it downt to 1 in a factorial way
    e.g if n is 5 then calculate 5*4*3*2*1 = 120
    n: is the highest starting number
    '''
    if n == 1:
      return True
    else:
      return n * factorial_recursive(n -1)

print(factorial_recursive(100))