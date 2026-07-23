'''
to find datatype--type(variable_name)
to find memory location--id(variable_name)
datatypes
----------
int
---
number=9
ex-number=9
for j in number
print(j)
float
-----
num=89.98
print(type(num))
string
------
ex--so = 'a1&,./?'
for j in so:
    print(j)
-->string is a sequence of char that are inclosed in('',"",''' ''')
-->str immutable
method(perenthisis imp for functions also)
------
replace()

used to replace old str with a new str
syntax-- variable_name.replace('old_str','new_str','how many number is optional')
ex-so = 'python is a language python python'
print(so.replace('python','java'))

ex--so = 'python is language'
print(so.replace('python','java'))
print(so)(java is a language)(python is a language) here the 1st sentence can not be modified)

join()
----
-->this method will add the new char after every sub-string
syntax--'new_string'.join(variable_name)

ex- so = 'python is a language'
print('-'.join(so))

split()
-------
ex-so = 'python is a language'
print(so.split('is'))

ex-2:time_ = '13.45'
parts_ = time_.split(':')
print(f'{int(parts_[0])-12} : {parts_

-->
index()-->position value
so = 'python is a language'
print(so.index('a'))
ex-2-so = 'python is a language'
print(so.count('n'))
ex-3-so = 'python is a language'
print(so.count('n',10,16))

---_indexing
ex-so = 'python is a language'
print(so[10])
list
----
-->list is the collection of different datatypes that are represented in []and seperated by, and list ia a mutable datatype
ex-any_ = [1,'python',[2,4]]
print(any_[2])
ex-2-any_ = [1,'python',[2,4]]
print(any_[1][2])
ex-3-any_ = [1,'python',[2,4]]
print(any_[2][1])
-->any_ = [1,'python',[2,['python',9],4],'java',['python',[54,78],'java',90]]
print(any_[4][1][0])
methods

append()
-->this method is used to add new item into the list and it will add at last index position
ex- any_ =[1,2,3,4,5]
any_.append(10)
print(any_)
any_.append(100)
print(any_)

extend()
-------
any_ =[1,2,3,4,5]
any_.append("python")
print(any_)
any_.extend("python")
print(any_)

remove()
--------
the method remove will del the item based on the value given if the value bot the list will the error
ex-any_ =[1,2,3,4,5]
any_.remove(2)
print(any_)

pop()
------
the method pop will del the item based on the index position given if the index position is out of range in the list will the error
'''

any_ =[1,2,3,4,5]
any_.pop(2)
print(any_)
