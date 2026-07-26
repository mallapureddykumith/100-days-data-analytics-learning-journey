'''
limit_ = int(input('enter the limit: '))
for j in range(1,limit_+1):
    if j % 2 == 0:
        print(f'{j} is a even')
    else:
        print(f'{j} is a odd')
ex-------
num = int(input('enter a num: '))
count = 0
for j in range(1,num+1):
    if num % j == 0:
        count += 1
if count == 2:
        print(f'{num} is prime')
else:
        print(f'{num} is not a prime')
ex----------------
for i in range(2,10):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f'{i} is prime')
ex-------------------

rev_ = input('enter word')
emp_ = ''
for j in rev_:
    emp_ = j + emp_
if emp_ == rev_:
    print(f'{rev_} is pal')
else:
    print(f'{rev_} not pal')
ex
-------------------
for
1
2
3
4
ex--start_ = 4
for j in range(1,start_+1):
    print(j)
ex
--------
*
**
***
****
ex
start_ = 4
for j in range(1,start_+1):
    for i in range(1,j+1):
        print('*',end='')...(end is used to give in horizontal in nxt value)
    print()

ex
---------------
1
12
123
1234
ex----------
1
23
456
78910
ex-count = 0
start_ = int(input("enter a num: "))
for j in range(1,start_+1):
    for i in range(1,j+1):
        count += 1
        print(count,end='')
    print()

ex--------
rverese
count = 0
start_ = int(input("enter a num: "))
for j in range(start_,0,-1):
    for i in range(1,j+1):
        count += 1
        print("&",end='')
    print()
ex---------
for pyrmid
num = 7
for j in range(num):
    print(" " * (num - j -1),end = '')
    print('* ' * (j+1))
ex------------
num = 7
for j in range(num,0,-1):
    print(" " * (num - j),end = '')
    print('* ' * j)

ex-------------------
nums = [1,2,2,5,5]
emt_ = []
for j in nums:
    if j not in emt_:
        emt_.append(j)
    print(emt_)

ex-num =6
per_num = 0
for j in range(1,num):
    if num % j ==0:
        per_num += j
if per_num == num:
    print(f'{num} is a per num')
else:
    print(f'{num} is not')

ex-1 where num = 6 or 28 or int(input('enter the num: '))
'''

num =6
per_num = 0
for j in range(1,num):
    if num % j ==0:
        per_num += j
if per_num == num:
    print(f'{num} is a per num')
else:
    print(f'{num} is not')

