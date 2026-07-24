'''
set
--------
-set is an unodered collection
-set do not  allows duplicate values inside it
-set mutable
-set is represented in{}
ex-do={1,2,3,4}
print(do)
ex-2d
o={1,2,3,4}
print(do)
#creating a empty set
so = set()
print(type(so))

method
------
1.update
-------
ex-do={1,2,3,4}
do.update([6,8])
print(do)

use to add new value into set

syntax-----variable_name.update(iterables)
ex- do={1,2,3,4}
do.update('python')
print(do)->o/p..python is ntohpy)

ex-2 do={1,2,3,4}
do.add('python')
print(do)
2.add
syntax-----variable_name.update(value)
ex-3 do={1,2}
do.add(4)
print(do)
3. remove
-- used to del the value from the set, incase if the value is not present
in the set will show key error
ex- 4do={1,2,4}
do.remove(4)
print(do)

discard
-------
used to del the value from the set, but never give any error incase value is not present insifde the set
ex-do = {1,2,3}
do.discard(4)
print(do)

5. pop()
------
used to del the value but this pop() will take 0 arguementss inside it 
ex-do = {1,2,3}
do.pop()
print(do)

operations
---------
ex-do = {1,2,3}
so = {3,4,5}
print(do|so)
1.union
------
give all sets value together but no duplicates
ex-
do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.union(so))

2.intersection
-----------
common vales in both sets
ex--do = {1,2,3}
so = {3,4,5}
print(do&so)
print(do.intersection(so)

3.difference
---------
ex- do = {1,2,3}
so = {3,4,5}
print(do-so)
print(do.difference(so))
ex-2 do = {1,2,3}
so = {3,4,5}
print(so-do)
print(so.difference(do))

type conversion
----------
Int :String;Float
ex--num=9
print(type(num))
so=str(num)
print(type(so))

float
----------
ex-num=9
print(type(num))
so=float(num)
print(so)
print(type(so))

float----

string--str()
ex-nums=8.89
print(type(nums))
all_=str(nums)
print(type(all_))

integer--
ex- nums=8.89
print(type(nums))
all_=int(nums)
print(all_)
print(type(all_))

string--

integer-- int()
--------
ex-1
how ="67"
print(type(how))
who = int(how)
print(type(who))
ex- 2
how ="67 is rupee"
print(type(how))
who = int(how)
print(type(who))

float---float()
ex--how ="6.87"
print(type(how))
who = float(how)
print(type(who))
      
list
-------------
ex-how ='[1,2,3,4]'
print(type(how))
who = list(how)
print(type(who))

ex-2 how ='2,3,4'
print(type(how))
who = list(how)
print(who)
print(type(who))

tuple
----------------
ex-how ='2,3,4'
print(type(how))
who = tuple(how)
print(who)
print(type(who))

list
------
string--str()
ex-nums =[2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))

tuple--tuple()
ex--nums =(2,3,4)
print(type(nums))
all_n = tuple(nums)
print(all_n)
print(type(all_n))

list---list()

string--str()
tuple -str
ex=--nums =(2,3,4)
print(type(nums))
all_n = str(nums)
print(type(all_n))

      

list-tuple
ex-nums =[2,3,4]
print(type(nums))
all_n = tuple(nums)
print(all_n)
print(type(all_n))
tuple -list
ex-nums =(2,3,4)
print(type(nums))
all_n = list(nums)
print(all_n)
print(type(all_n))

(+)
ex- num=9
num_2=8
print(num + num_2)
ex--
num=9
num_2=8
print(num + num_2)

any_ = 'python is a'
we = ' language'
print(any_+we)

nums=[1,2]
all_=[3,4]
print(nums+all_)


'''
num=9
num_2=8
print(num + num_2)

any_ = 'python is a'
we = ' language'
print(any_+we)

nums=[1,2]
all_=[3,4]
print(nums+all_)


      
