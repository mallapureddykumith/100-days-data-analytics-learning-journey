'''
elif
-----
ex-1
marks_ = 78
if marks_ >= 90:
    print('A+')
elif marks_ >= 80:
    print('A')
elif marks_ >= 70:
    print('B+')
elif marks_ >= 60:
    print('B')
elif marks_ >= 50:
    print('C+')
elif marks_ >= 40:
    print('C')
else:
    print('fail')

ex-2
marks_ = int(input("enter your marks"))
if marks_ >= 90:
    print('A+')
elif marks_ >= 80:
    print('A')
elif marks_ >= 70:
    print('B+')
elif marks_ >= 60:
    print('B')
elif marks_ >= 50:
    print('C+')
elif marks_ >= 40:
    print('C')
else:
    print('fail')

ex-
num = 89
num_2 =102
num_3 =5
if num> num_2 and num > num_3:
    print(f'{num} is greater value')
elif num_2 > num and num_2 > num_3:
    print(f'{num_2} is greater value')
else:
    print(f'{num_3} is greater value')

--> nested if
-----------------

EX- detail_ = {'ATMPIN': '9870'}
atm_ = input('enter tour 4 digit atm pin: ')
if len(atm_) ==4:
    if atm_ ==  detail_['ATMPIN']:
        OP_ == int(input("enter \n1.Withdraw \n2.Deposite \n3.pinchange"))
        if OP_ ==1:
            money_W = int(input('enter money to withdraw: '))
        elif OP_ ==2:
            money_D = int(input('enter money to deposite: '))
    else:
        print('incorrect pin entered')
else:
    print('pls eneter only 4 digit pin')
    ex-num = 'python is a language'
for i in num:
    print(i)
else:
    print('end')


CONTROL STATEMENTS
ex-num = 'python is a language'
for i in num:
    print(i)
else:
    print('end')

break
--------
ex-num = [34,67,90]
for i in num:
    print(i)
    if i == 90:
        break
else:
    print('end')
CONTINUE
------
ex-num = [34,67,90]
for i in num:
    if i == 90:
        continue
    print(i)
    
else:
    print('end')

PASS
---------
ex- num = [34,67,90]
for i in num:
    pass

LOOPS
---
1. for loop
---------
--> for loop is used to itterate over sequence such as str, list, tuple
-->else in for loop it will execute when whole itterates are completed
-->incase if condition becomes true, then else will never execute

-->RANGE()
range() function is used togenerate number upto a limit
synatx-- rnage(start, end, step)
ex-for j in range(1,10,3):
    print(j)

2.while loop
------------------
infinty loop ex
num = 1
while num< 10:
    print(num)
ex--num = 1
while num< 10:
    print(num)
        num += 1
ASSERT KEYWORD
-----------------
the keyword is used to check the condition
ex-age =35
assert age >= 18, 'not eligible'
print('eligible')
ex-marks =35
assert marks >= 18, 'fail'
print('pass')



'''

time_ = '13.45'
parts_ = time_.split(':')
print(f'{int(parts_[0])-12} : {parts_}}
