'''
output foramgting
---------------]]
name = 'samyu'
age = 20
print('welcome',name,'your age is',age)

2. f-string (doc-string)
---------------------
name = 'samyu'
age = 20
print(f'welcome {name} your age is {age}')
%
-----
 %s--->all
 eg-name = 'samyu'
 print('name : %s' % name)

 %d--->digit
 eg-price = 89.9
print('name : %d' % price)

 %f--->float
 price = 89.9
print('name : %f' % name)
eg--name = 'samyu'
price = 89.9
print('name :  {}'.format(name))
ex----name = 'samyu'
age = 89
print('name :  {} \nage : {}'.format(name,age))

-->what are the statements

1. condition(if, if else, elife, nested if)
2. control(break, continuous, pass)
3. loop(while, for)

if condition
-----------
the if condition is used to check it is true or false
eg--
age = 18
if age >= 18:
    print(f"your age is {age} and eligible to vote")

if-else
---------
--> else is the fall back statement, incase if condition is false then this else block will execute

eg--age = int(input("enter your age: "))
if age >= 18:
    print(f"your age is {age} and eligible to vote")
else:
    print(f"your age is {age}, you have to wait {18 - age} years")

ex--2
num = int(input("enter a number: "))
if num % 2 ==0:
    print(f'{mnum} is a even number')
else:
    print(f"{num} is a odd number'))

ex-3
vol_ = input('enter single letter: ')
if vol_ in 'AEIOUaeiou':
    print(f'{vol_} is vol')
else:
    print(f'{vol_} is con')

eg-4
so = 'python'
do = so[::-1]
print(do)
if so[::-1 == so:
    print(f'{so} is a palli')
else:
    print(f'{so} not a palli')
ex-5
so = 'python'
do = so[::-1]
print(do)
if so[::-1] == so:
    print(f'{so} is a pali')
else:
    print(f'{so} not a pali')

ex-6

year_ = int(input("enter a year: "))
if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
    print(f'{year_} is a leap')
else:
    print(f'{year_} not a leap')
  
'''
year_ = int(input("enter a year: "))
if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
    print(f'{year_} is a leap')
else:
    print(f'{year_} not a leap')
  

