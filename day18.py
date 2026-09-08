'''
inheritance
---------
--> inheritance is the process of inherite one class into another class
--> will generally inherite from a class is called parent class and using it in another that class i s called child class
ex---class company: 
    def salary(self): 
        print('company salary')
class employee(company): 
    def mon_sal(self): 
        print('employee salary')
per_sal = employee()
per_sal.mon_sal()
per_sal.salary()

types
-----------------
1. single inheritance
------------------------
-> if one child class inherite from one parent class this is called single inheritance
ex-class father:
    def land(self):
        print('5 acer land')
class me(father):
    def flat(self):
        print('6 flat')
all_ = me()
all_.flat()
all_.land()

ex-2

class doctor:
    def patient(self):
        print('tablets')
class me(doctor):
    def homeo_medi(self):
        print('5 tablets')
all_ = me()
all_.homeopathi()
all_.patient()
2. multiple inheritance
-----------------------
->if one child inherite from more than one parent class this is called multiple inheritance
ex--class father:
    def home(self):
        print('home at village')
class mother:
    def gold(self):
        print('50kg gold')
class son(father, mother):
    def flat(self):
        print('sons flat')
all_to = son()
all_to.home()
all_to.gold()

3. multi-level inheritance
-------------------------
->one child class become parent class to the another  is callled multi-level inheritance
ex-class grandfather:
    def land(self):
        print('grandfather land')
class father(grandfather):
    def flat(self):
        print('father flat')
class son(father):
    def car(self):
        print('sons car')
fam = son()
fam.land()
fam.flat()
fam.car

4. hierchical inheritance
------------------------
-> if two child class inherite from one parent is called as hierchical inheritance
ex--class father:
    def land(self):
        print('50 acer land')
class son_1(father):
    def flat(self):
        print('first son flat')
class son_2(father):
    def car(self):
        print('second son car')
class son(father):
    def car(self):
        print('sons car')
s1 = son_1()
s1.land()
s1.flat
s2 = son_2()
s2.land()
s2.car
5. hybrid inheritance
-------------------------
->inherite from more than two types into one class is called as hybrid inheritance
ex-class person:
    def name(self):
        print('julie is her name')
class student(person):
    def study(self):
        print('b-tech final year')
class py_teacher:
    def teach(self):
        print('python')
class java_teacher:
    def teach(self):
        print('java')
class learner(py_teacher,java_teacher):
    def learn(self):
        print('learner')
class all_get(student,learner):
    def get_it(self):
        print('this person is getting all the data')
an = all_get()
an.name()
an.study()
an.teach
an.learn()
an.get_it


super() method
-----------------
->this super() method is used to get the constructor from the parent class and use in the child class

->and also can get any method from the class..
ex--

class person:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role
class employee(person):
    def __init__(self,name,age,salary,role):
        super().__init__(name,age,role)
        self.salary = salary
        print('employee constructor called')
obj = employee('sufi',18,100,'python developer')
print(obj.name)
print(obj.age)
print(obj.salary)

ex-class all_:
    def job_(self):
        print("i am looking for a job")
class looking(all_):
    def job_in(self):
        super().job_()
        print('we are looking for a candidate')
    def an_(self):
        super().job_()
        print('no jobs')
any_ = looking()
any_.an_()

ex-class all_:
    def job_(self):
        print("i am looking for a job")
class looking(all_):
    def job_(self):
        super().job_()
        print('we are looking for a candidate')
any_ = looking()
any_.job_()

POLYMORPHISM
------------
->polymorphism means a same name but different forms...

1.METHOD OVERLOADING
----------------------
->this method overloading happens in a class a method is created with this same name, but the recent method will be activated and the before one will not the considered 
ex-class data_:
    def add_(self,a,b,c=0):
        return a+b+c
    def add_(self,a,b,c):
        return a+b+c
    def add_(self,a,b,c,d):
        return a+b+c+d
obj = data_()
print(obj.add_(2,3,9,7))

2.METHOD OVERRIDING
--------------------------

->this method overriding happens when a parent class and child class have same method and the child class takes its own implimentation
ex-class pay:
    def payment(self):
        print('payment called')
class UPI(pay):
    def payment(self):
        print('UPI payment called')
class paytm(pay):
    def payment(self):
        print('paytm payment called')
obj = UPI()
obj.payment()
go = paytm()
go.payment()


3.OPERATION OVER.LOADING
-------------------------
->operator overloading which gives the special meaning to theoperator when it is called by the object
1.__add__

ex-class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __add__(self,do):
        print(self.any_ + do.any_)
how = cal(55)
who = cal(66)
how.__add__(who)

ex-class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __add__(self,do):
        print(self.any_ + do.any_)
how = cal(55)
who = cal(66)
how.__add__(who)
print(how+who)



2.__Sub__

ex-class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __sub__(self,do):
        print(self.any_ + do.any_)
how = cal(55)
who = cal(66)
print(how-who)


3.__mul__

ex-class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __mul__(self,do):
        print(self.any_ + do.any_)
how = cal(78)
who = cal(67)
print(how*who)

4.__truediv__

ex-class cal:
    def __init__(self,any_):
        self.any_ = any_
    def __truediv__(self,do):
        print(self.any_ + do.any_)
how = cal(78)
who = cal(67)
print(how/who)


ABSTRACTion
--------------
->Abstarction means hiding the implemented data and showing only need data to user 
ABC ->abstract base class
-the abstract method is used to hide that particular information of a base class

from abc import ABC,abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('government interest is 3.5')        
class SBI_bank(gov_bank):
    def interest(self):
        print('SBI bank interest is7.8')
class ICIC_bank(gov_bank):
    def interest(self):
        print('ICIC bank interst is 8.9')
obj = SBI_bank()
obj.interest()
obje = ICIC_bank()
obje.interest()


from abc import ABC,abstractmethod
class cls_fee(ABC):
    @abstractmethod
    def fee_str(self):
        print('college fee 45000')
class manag(cls_fee):
    def fee_str(self):
        print('college fee 100000')
class EM_(cls_fee):  
    def fee_str(self):
        print('college fee 15000')
PRACTICE SESSION
EX-class Calculator:

    def add(self, *numbers):
        return sum(numbers)


calc = Calculator()

print(calc.add(10, 20))       
print(calc.add(10, 20, 30, 40))


#or

class Calculator:

    def add(self, a, b, c, d=None):
        if c is None:
            return a + b
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))       
print(calc.add(10, 20, 30))   

REGULAR EX[PRESSSION(regEx)
----------------------------
->this RegEx is used from a search pattern to find out the sting contain sequence char or not
->to use this RegEx, we need to import re module

FUNCTIONS
------
Findall
-----------------
the searching pattern is found then it will gives the output in the list []
ex-1
import re
some = 'python is a programming language'
print(re.findall('^python', some))
ex-2
import re
some = 'python is a programming language'
print(re.findall('[a]', some))

Search
------
-> this is also is use to form a searching pattern , but it will give only the first matchedd object
-->where it will gives the index position, where the matched object is found by the pattern
ex-1
import re
do='i have 1000 ruppees with me'
print(re.search('e',do))

meta characters
-------
->meta characters are the symbols used in the search pattern
1. []
-> this [] symbol is used to find a grp of char that are present in the str,where we can also specify the range
->syntax-re.findall('[r]',variable_name)
->by using this symbol we can search cap(A-Z), small(a-z)and digits(0-9)
ex-
import re
some='we are in the class 90o0gdudhdidhihu'
print(re.findall('[a-z]',some))
print(re.findall('[A-Z]',some))
print(re.findall('[0-9]',some))
print(re.findall('[augoo]',some))
print(re.search('[a-z]',some))

2. 
--------------
.char-.he__o
->this symbol will refer only one means can match only a single char in the pattern ....
syntax--> re.search('C...',variable_namme))
ex-import re
some='Hello! World'
print(re.findall('H...o',some))
print(re.search('H......',some))


3. +
---------
->the symbol max bnumber of sequence from the string from atleast one character
syntax-re.findall('.+',variable_name)
ex-
import re
some = 'The symbol is used to find a group char that present'
print(re.findall('T.+e',some))



4. ^
----------
->this symbol is used to find the pattern where the string starting match or not
syntax->re.findall('^',variable_name)
ex-
import re
some='Hello! World'
print(re.findall('^Hello',some))
print(re.search('^Hello',some))


5. $
--------------
->this symbol will find out if the string is ending with patttern or not
syntax->re.findall('sequence$',variable_name)
ex-
import re
any_='I am planning for a trip'
print(re.findall('for a trip$',any_))
print(re.search('for a trip$',any_))

6. ?
-----
->the symbol will find max upto 1 match in the string
syntax-re.findall('.?'variable_name)
ex-import re
some = 'Hello! World Hello:'
print(re.findall('Hel.?o',some))



7. *
---------
the symbol max number of sequence from the string
syntax->re.findall('.*',variable_name)
ex-import re
some = 'the symbol is used to find a group char that present'
print(re.findall('T.*r',some))


8. {}
---
->the symbol is used to find a vroup char that present in string
syntax--> re.findall('E.{size}',variable_name)
ex-import re
all_='I have 1000 rupeees with me'
print(re.findall('I.{2}',all_))

ex-import re
user_name = input("please enter your name:")
pattern = re.search('^[A-Z,a-z]{3,}$',user_name)
if pattern:
    print('correct')
else:
    print('incorrect')

ex---
import re
num = input("please enter your number:")
fnd = re.findall('^[6-9][0-9]{9}$',num)
if fnd:
    print('indian')
else:
    print('not indian')

ex-import re
some = 'Hello! World Hello:'
print(re.findall('Hel.?o',some))




'''











