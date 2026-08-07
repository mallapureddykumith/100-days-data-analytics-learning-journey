'''import random
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# asscii_letters--> this string module functionn that can give
#upper and lower letters
#digits-> strings module function that can give number(0-9)
punctuation->this string module function can give us
#punctuations (&$@)
ex-print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
ex-import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_chars = letters + digits + punctuation
password = ''
for i in range(5):
    password += random.choice(all_chars)
    print(password)
ex-import random
import string
letters = string.ascii_letters
digits = string.digits
special_char = '@#$*'
all_chars = letters + digits + special_char
password = ''
for i in range(5):
    password += random.choice(all_chars)
print(password)
ex--

bank_balance = 10000
from datetime import datetime
import sys
now = datetime.now()
while True:
    print("----welcome to axis atm----")
    user_opt = int(input("\n1.withdraw\n.deposite \n3.check balance\n4.exit:"))
    if user_opt == 1:
        with_m = int(input('enter the money you want to withdraw'))
        if with_m > bank_balance:
            bank_balance -=with_m
            print(f'remaining money {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
        else:
            print('insufficient money')
    elif user_opt ==2:
        deposite_m = int(input('enter the money you want to deposite'))
        bank_balance += deposite_m
        print(f'money addded successfully: {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
    elif user_opt == 3:
        print(f'available balance: {bank_balance} {now.strftime("%H:%M %Y-%m-%d")}')
    elif user_opt == 4:
        sys.exit()
    else:
        print("incorrect choice")
        print('thankyou for visiting the atm')
        sys.exit()
ex---
import random
num = random.randint(1,100)
user_opt = int(input("pick a number(1-100): "))
if user_opt == num:
    print(f'you have picked {user_opt} number')
else:
    print('better luck next time')

day-17

Exception handling
------------------
-> an error can be handled by try and except
1.try:
-----------------
we can check the cde  here which may contain any error
ex-try:
    print(n)
except:
    print('error')
    
2.exception:
=------------
->exception cn handle any error that come in the try block
ex-
try:
    num = 0
    num_2 = 6
    print(num_2/num)
except:
    print('will get an error')
num = 8
num_2 = 0
print(num/num_2)
        
ex-try:
    any_ = int(input('enter any number:'))
    print(any_+9)
except:
    print('error')
ex-try:
    print(9+'python')
except:
    print('error')

ex-try:
    print(9+1)
except:
    print('error')
else:
    print('no error')


3.else:
->if no error in the code were raised, then the else block will execute
ex-try:
    print('python'+9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise ZeroDivisionError')
except NameError:
    print('this will raise NameError')
except TypeError:
    print('this will raise TypeError')
else:
    print('no error')


4.finally:
the finally block will execute if error present in the try block or not

ex-try:
    print('heyyy')
except ZeroDivisionError:
    print('this will raise ZeroDivisionError')
except NameError:
    print('this will raise NameError')
except TypeError:
    print('this will raise TypeError')
else:
    print('no error')
finally:
    print('end')
    
ex-try:
    print('heyyy')
except ZeroDivisionError:
    print('this will raise ZeroDivisionError')
except NameError:
    print('this will raise NameError')
except TypeError:
    print('this will raise TypeError')
else:
    print('no error')
finally:
    print('end')
file handling
-------
->an file handler is an object used to connect with that particular file
1. with(keyword)
by using with keyword no need to close the file ,it will close it by itself
syntax-
---------
BY FILE NAME SYNTAX
with open('file_name','mode') as name:
BY FILE PATH SYNTAX
with open(r'file_path','mode') as name:
ex-with open('demo.txt','r') as file_:
    print(file_.read())

2. open(keyword)
by using this open() we have to close the file by using close
ex-any_ = open('demo.txt','r')
print(any_.read())
any_.close()

modes
-----------------------------
1. 'r'
------------------
the 'r' mode is used for functions read(),readline() and readlines()
ex-ex-with open('demo.txt','r') as file_:
    print(file_.read())

ex-
2. 'w'
---------
the 'w' mode is used for write() function
ex-with open('demo.txt','w') as file:
    file.write('python module take 5 hour per day')



3. 'a'
ex-with open('demo.txt','a') as file:
    file.write('python module take 5 hour per day')

4. 'x'

function
[--------
1.write()
ex-with open('demo.txt','w') as file:
    file.write('python module take 5 hour per day')

2.read()
ex-with open('demo.txt','r') as file:
    print(file.read(20))
    
3.readline()
ex-with open('demo.txt','r') as file:
    print(file.readline())
-------
4.readlines()
-----------
the readlines() will read whole file and written it in a list, where each line is one index in the list
ex-with open('demo.txt','r') as file:
    print(file.readlines())
    


'''

with open('demo.txt','r') as file:
    print(file.readline())
    























