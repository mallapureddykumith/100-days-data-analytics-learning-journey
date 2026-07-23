'''
tuple
--------
--> tuple is a collection of datatype that are represented in () and separated by,
-->tuple is immutable
eg--go = (1, 'java', [3,4],('python',78))
print(go.index('java'))

count()
------------
syntax--variable_name.count(item)
go = (1, 'java', [3,4],('python',78))
print(go.count(('python',78)))---o/p-->1
print(go.count('python'))---o/p-->0

dictionary
----------
-->dict is a key:value pair
-->keys and values separated by:
-->dict is represented by{}
-->keys must be immuttable datatypes
methods
-
1.keys
-----------
syntax--dict.keys()
ex--details={'name':'teja',
         'ac':23456789,
         'pan':34567890,
         'adhar':987654321,
         'pin':1234}
print(details.keys())


2.values
------------
syntax--dict.values()
ex--details={'name':'teja',
         'ac':23456789,
         'pan':34567890,
         'adhar':987654321,
         'pin':1234}
print(details.values())

3.items
--------
shyntax--dict.items()
4. update
------
syntax-- dict.update({key:values})
eg--details={'name':'teja',
         'ac':23456789,
         'pan':34567890,
         'adhar':987654321,
         'pin':1234}
details.update({'gender':'male'})
print(details)
eg-2
details={'name':'teja',
         'ac':23456789,
         'pan':34567890,
         'adhar':987654321,
         'pin':1234}
details.update({'gender':'male'})
details.clear()
print(details)

'''

details={'name':'teja',
         'ac':23456789,
         'pan':34567890,
         'adhar':987654321,
         'pin':1234}
details.update({'gender':'male'})
details['name']='garikapati'
print(details)
