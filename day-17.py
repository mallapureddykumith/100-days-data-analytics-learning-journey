'''run_assistant()

oops
-----
->object oriented programming system
->OOps is used to maintain the code structure in object and classes..

1.class
-------
-> class is an blue print or templet to an object
syntax
---------
class(keyword) name:
class func:
    #attribute
    #methods
2.object
->object is instance of the class
syntax
--------
class(keyword) name:
    #attribute
    #methods
    any_ = class_name
ex-class person:
    name = 'kumith'
    Edu = 'B.tech'
p1 = person()
print(p1.name)

ex-class stu:
    name = 'kumith'
    age = '20'
s1 = stu()
print(s1.name)
print(s1.age)
    
ex-class codegnan:
    city = 'hyd'
    tech = 'python'
    data_ = 'MYSQL'
code = codegnan()
print(code.city)



3.attribute
---------
-> attribute is the data present in the class or pass to the classs
ex-
take car
[-----
colour
brand
seat
ex-class kumith:
    name = 'kumith'
    age = '20'
    Back_G = 'b-tech'
an = kumith()    
print(an.name)
ex-ex-class kumith:
    name = 'kumith'
    age = '20'
    Back_G = 'b-tech'
an = kumith()    
print(an.name)
ex-class det:
    def __init__(self):
        self.name = 'ethan'
        self.age = 6
        self.back_g = 'B-tech'
        self.role = 'student'
person_ = det()
print(person_.name)
print(person_.age)
print(person_.back_g)
print(person_.role)

ex-class bank_details:
    def __init__(self):
        self.name = 'thabitha'
        self.aadhar_number = '52918526901'
        self.account_number = '5646546456'
        self.ifsc_code = 'sjds648645'
        self.num = 5648973124
person_ = bank_details()
print(person_.name)
print(person_.aadhar_number)
print(person_.account_number)
print(person_.ifsc_code)
print(person_.num)



4.methods
-----------
->method is a function that is created inside the classs
syntax
----
class(keyword) name:
    #attributes
    def fun_name(self):
        #code
obj = class_name()
print(obj.fun_name())
ex-class student:
    def __init__(self):
        self.name = 'ethan'
        self.age = 6
        self.course = 'DA'
    def st_name(self):
        print(self.name)
        print(self.age)
        print(self.course)
    def all_data(self):
        print(self.name)
        print(self.age)
stu_= student()
stu_.st_name()
stu_.all_data
        
ex-class car:
    def __init__(self):
        self.colour = 'blue'
        self.seat = 6
        self.brand = 'BMW'
    def brake_(self): 
        print(f'{self.brand} brake will apply at speed 250KM')
    def accelater_(self): 
        print(f'{self.brand} will take 2 sec to reach 180 speed')
    def clutch(self):
        print(f'{self.brand} with {self.seat} automatic')
BMW = car()
BMW.brake_()
BMW.accelater_()
BMW.clutch()
        
ex-class students:
    def __init__(self,name,age,batch):
        self.name = name
        self.age = age
        self.batch = batch
    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)
stu_1 = students('julie',18,5)
stu_1.all_data()
stu_2 = students('ethan',7,5)
stu_2.all_data()

ex---class registration:
    def __init__(self,name,age,number,aadhar,pan,ifsc):
        self.name = name
        self.age = age
        self.number = number
        self.aadhar = aadhar
        self.pan = pan
        self.ifsc = ifsc
    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.number)
        print(self.aadhar)
        print(self.pan)
        print(self.ifsc)
reg_1 = registration('julie',18,5454546554,'564564656','hj564545','uu5645644')
reg_1.all_data()
reg_2 = registration('ethan',5,'5454654544','6489456456','sg86465','h6446546545')
reg_2.all_data()

ex-class registration:
    def __init__(self,name,age,number,aadhar,pan,ifsc):
        self.name = name
        self.age = age
        self.number = number
        self.aadhar = aadhar
        self.pan = pan
        self.ifsc = ifsc
    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.number)
        print(self.aadhar)
        print(self.pan)
        print(self.ifsc)
reg_1 = registration('julie',18,5454546554,'564564656','hj564545','uu5645644')
reg_1.all_data()
reg_2 = registration('ethan',5,'5454654544','6489456456','sg86465','h6446546545')
reg_2.all_data()

->oops is used to organize the code
->CONSTRUCTER
------------
-> __init__
->the constructer is a special method that only run when the object is created
->mostly we will take data inside this method...
ex---class cls_data:
    def __init__(self):
        self.name = 'sufi'
        self.course = 'python'
cls_ = cls_data()
print(cls_.name)
print(cls_.course)

SELF
--------
->the self keyword reffers to current object
ex-class stu:
    def __init__(self):
        self.name = 'sufi'
    def any_(self):
        print(self.name)

ex-class stu_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')
data1 = stu_data('sufi',123,33)
data1.student()

encapsulation
---------------
->wrapping data and methods together is called as encapsulation and using or controlling the data in methods 

ex-class stu_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')
data1 = stu_data('sufi',123,33)
data1.student()

access specifiers
-----------
1.public (name)
------------
this can be access normally and can call it like a normal variable
ex-self.name = name
print(self.name)

ex-class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = name
        self.batch = batch
        self.age = age
        self.fee = fee
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age} paid {self.fee}')
data1 = stu_data('sufi',123,33,4500)
data1.student()

2.proctected (_name)
------------------
-> just adding single(_) before a variable it becomes protected variable

ex-self._age = age
print(self._age)

ex-class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = name
        self.batch = batch
        self.age = age
        self._fee = fee
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age} paid {self._fee}')
data1 = stu_data('sufi',123,33,4500)
data1.student()

ex-class stu_data:
    def __init__(self,name,batch,age,fee):
        self._name = name
        self._batch = batch
        self._age = age
        self._fee = fee
    def only_name(self):
        print(f"{self._name}")
    def only_batch(self):
        print(f"{self._batch}")
    def only_age(self):
        print(f'{self._age}')
    def only_fee(self):
        print(f'{self._fee}')
data1 = stu_data('sufi',123,33,4500)
data1.only_name()
data1.only_batch()

3.private (__name)
-----------------
->adding (__) before a variale it becomes private variable

ex-self.__balance = balance
print(self.__balance)
ex--class bank_ac:
    def __init__(self):
        self.name = 'sufi'
        self.adh = '78686879697'
        self.pan = 'gf56r5767'
        self.__balance = 45000
    def details(self):
        print(self.name)
        print(self.adh)
        print(self.pan)
    def bank_bal(self):
        print(self.balance)
AC = bank_ac()
AC.details()
ex--class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = name
        self.batch = batch
        self.age = age
        self.__fee = fee
        
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age} paid {self.__fee}')
data1 = stu_data('sufi',123,33,4500)
data1.student()

ex-class employee:
    def __init__(self):
        self.name = 'sufi'
        self.role = 'python developer'
        self.__salary = 44600 
        self._experience = 4.5
        self._emptype = 'full-type'
        
    def details(self):
        print(self.name)
        print(self.role)
        
    def income_(self):
        print(self.__salary)
        
    def type_(self):
        print(self._experience)
        print(self._emptype)
emp = employee()
emp.details()
emp.income_()
emp.type_()











'''

class bag:
    def __init__(self):
        self.eng_book = 'fairy tail'
        self.hindi_book = 'bhay'
        self.__salary = 44600 
        self._experience = 4.5
        self._emptype = 'full-type'
        
    def details(self):
        print(self.name)
        print(self.role)
        
    def income_(self):
        print(self.__salary)
        
    def type_(self):
        print(self._experience)
        print(self._emptype)
emp = employee()
emp.details()
emp.income_()
emp.type_()



















