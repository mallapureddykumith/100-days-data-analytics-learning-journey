'''
modules
----------
-modules are the python code which is saved in(.py)that contains functions, variables, classes
1. built-in
-----------
->the built-in modules that are already designed which comes with python when we are installing
ex:
-
1. math
2. sys
3. os
4. randam

2. user-defined
-------------------
->the user defined modules are created by the programmer
syntax->import(keyword) module_name

ex-import first_module
print(first_module.add(56,8))
print(first_module.subtract(56,8))

-we can also import a module with different name
-after importing with the alias name, we have to use that alias anme in the code

ex-import first_module as am
print(am.add(56,8))
print(am.subtract(56,8))

importing only need function
----------------------------
->when we are importing the few functions from the module can only access that function
syntax-> from(keyword) module_name import(keyword) functions
ex-from first_module import add,mul
print(add(56,8))
print(mul(6,8))

importing all functions
-----------------------
->use the all function in that module we hve to use(*) to get all of those..
sayntax-> from(keyword) module_name import(keyword)*)
ex-from first_module import *
print(add(56,8))
print(mul(6,8))
print(subtract(56,8))
print(div(6,8))
print(pow(3,8))

ex-import first_module
first_module.display()
print(f'welcome{name}')

ex- for in built---import random
print(random.randint(1000,2050))

ex-import math
print(math.sqrt(25))

ex-import sys
print(sys.version)


details = {
    'name' : 'kumith',
    'ATM PIN' : '2005'
}
import random
remain_ =3
while remain_ > 0:
    pin_ = input('enter pin number: ')
    if pin_ == details['ATM PIN']:
        otp = random.randint(1000,9999)
        print(otp)
        user_otp = int(input('enter user otp: '))
        if user_otp == otp:
            opt = int(input('enter option \n1.withdraw \n2.deposite'))
    else:
        remain_ -= 1
        if remain_>0:
            print(f"incorrect pin entered and you have {remain_}")
        else:
            print(f"you have entered 3 times incorrect pin car")
math
-----------
-> math module used to work on mathematical functionlity

floor
--------
it will round-down to the near value..

ex-import math
print(math.floor(3.78))
print(math.ceil(3.78))
ex-2
-----
import math
print(math.gcd(24,30))

lcm-ex-
import math
print(math.lcm(24,30))
it will get the sqrt value
ex-import math
print(math.sqrt(25))

fctorial
--------
it will give factorial value.. 
import math
print(math.factorial(5))

ex-import math
print(math.log(5,6))
print(math.cos(math.pi))
print(math.pi)

random
------
-> the random module used to get random number
ex-import random
print(random.randint(1,600))
CHOICE
-------------------------
ex-2
import random
colour = ['red','green','blue','yellow','black']
print(random.choice(colour))

->it will the random value from the given data
shuffle
-----------------------
->it can shuffle the data randomly

ex-import random
colour = ['red','green','blue','yellow','black']
print(random.choice(colour))
random.shuffle(colour)
print(colour)
uniform
---------
-> will give the decimal values in a range given 
ex-import random
print(random.uniform(1,100))
ex- import sys
print(sys.version)
version
-------------------
the version of python interpreter
path
------
->.py path we will get by this function
ex-import sys
print(sys.version)
print(sys.path)
exit-
->this function will exit from the program
ex-import sys
print(sys.exit())
platform
--------
->it will gives the python run platform

argv
-----
-> it will give the current file run path
import sys
print(sys.argv)
datetime
->it will give the today time+date
ex-from datetime import datetime
print(datetime.now())
ex-2
from datetime import datetime
print(datetime.now())
print(datetime.today)
ex--from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%M-%D'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%H-%M-%S'))


%Y--> will get the year
%m---> will get the month
%D---> will get the day
%M---> will get the minute
%A--> CURRENT DAY
%B--> CURRENT MONTH
COLLECTIONS
--------------------
-> THE collections module will provide containeer type data which is more powerful than built-in data types(dict,list,tuple)
ex-import collections
data = ['apple','banana','orange','banana','pineapple']
print(collections.Counter(data))

deque
-------------
->userd to work with list
ex-from collections import deque
how = deque([1,2,3])
how.appendleft(7)
print(how)
ex-from collections import deque
how = deque([1,2,3])
how.extend([4,5,6])
print(how)

ex-from collections import deque
how = deque([1,2,3,4,5])
how.pop()
print(how)
ex-from collections import namedtuple
data= namedtuple("stu",('name','age'))
print(data('john','18'))
ex-from  itertools import count
c = count(100)
for j in range(5):
    print(next(c))
->import itertools
for j in itertools.repeat('python',10):
    print(j)
ex-from itertools import permutations
data = permutations([1,2,3],2)
print(list(data))

ex-any_ = combinations([1,2,3],2)
print(list(any_))

'''
import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())

