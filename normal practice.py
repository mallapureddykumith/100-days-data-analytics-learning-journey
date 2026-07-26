'''
# Increasing pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Decreasing pattern
for i in range(3, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
7x1 = 7
7x2 = 14
ex--tab_ = 7
for j in range(1,11):
    print(tab_) .....o/p will be only 7 in 10 times

ex--tab_ = 7
for j in range(1,11):
    print(f'{tab_} x {j} = {tab_*j}')
ex for any table--tab_ = int(input('enter a num: '))
for j in range(1,11):
    print(f'{tab_} x {j} = {tab_*j}')

152 = 1**3+5**3+3**3
amstrong ex-
num = 1
length_ =len(str(num))
am_ =0
for j in str(num):
    am_ = int(j) ** length_ + am_
if am_ == num:
    print(f'{num} is amstrong')
else:
    print(f'{num} is not')

    
ex----limit_ = int(input('enter limit: '))
num = 0
num_2 = 1
print(num,num_2,end= ' ')
for j in range(1,limit_+1):
    all_ad = num+num_2
    num = num_2
    num_2 = all_ad
    print(all_ad,end=' ')

ex-----calculator
num_1 = int(input('enter a num: '))
num_2 =int(input('enter a num: '))
opt_ = int(input('enter \n.add \n.sub: '))
if opt_ == 1:
    print(num_1 + num_2)
elif opt_ == 2:
    print(num_1 - num_2)

'''
AXIS_bank_kumith = {'name':'kumith',
                    'adhar':'352918529601',
                    'ATM PIN':'2005',
                    'balance':8900}
remain_amount = 3
while remain_amount >0:
    pin_ = input("enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in AXIS_bank_kumith['ATM PIN']:
            opt_ = int(input('enter \n.withdrw \n.deposite \n3.balance: '))
            if opt_ ==1:
                withdraw_m = int(input('enter the amount you want to withdraw: '))
                if withdraw_m <= AXIS_bank_kumith['balance'] -= withdraw_m % 100 ==0:
                    AXIS_bank_kumith['balance'] -= withdraw_m
                    print(f'you have withdraw{withdraw_m} and the total balance amount')
                    break
                else:
                    print('can not provide change or no balance')
                    break
            elif opt_ ==2:
                pass
            elif opt_ ==3:
                pass
            
        else:
            remain_amount -= 1
            if remain_amount >0:
                print(f'incorrect pin and you have only {remain_amount}')
            else:
                print('card is block')
                break
    else:
        print('pls enter only 4 digit atm pin')
