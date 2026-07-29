'''
function
--------
a function is a block that can be excutes when we call it
to avoid therepeated lines of code
ex--
def function_name (arguements)
types of functions
---
1built-in
ex-
print()
len()
max()
min()
2. user-define
----------
user-define are the functions that are develop by the user
ex-num = 56
num_2 = 891
def total_(num, num_2):
    print(num +num_2)
total_(num, num_2)
total_(1,2)

required arguements
------
we have to pass same number arguemnets that match in the parameters
ex-num = 56
num_2 = 891
def total_(num, num_2):
    print(num + num_2)
total_(num, num_2)
total_(1,2,3)


positional arguements
-----------------
it doesnt matter how we are passing the variable, if we assign the value to that variable in the calling
ex-
def name_(name, name_):
    print(name)
    print(name_)
name_(name = 'kumith' , name_ = 'samyu')
ex--------
def pos_(m,n,b,v,c):
    print(n)
pos_(m=0,n=2,b=3,v=4,c=6)
'''

AXIS_bank_kumith = {'name':'kumith',
                    'adhar':'352918529601',
                    'ATM PIN':'2005',
                    'balance':'8900',
                    'transaction history:[]}
remain_amount = 3
while remain_amount >0:
    pin_ = input("enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in AXIS_bank_kumith['ATM PIN']:
            opt_ = int(input('enter \n.withdrw \n.deposite \n3.balance: '))
            if opt_ ==1:
                withdraw_m = int(input('enter the amount you want to withdraw: '))
                if withdraw_m <= AXIS_bank_kumith['balance'] and withdraw_m % 100 ==0:
                    AXIS_bank_kumith['balance'] -= withdraw_m
                    print(f'you have withdraw{withdraw_m} and the total balance amount')
                    print("Current Balance:", AXIS_bank_kumith['balance'])
                    user_ = int(input('enter \n1.home page \n2.exit: '))
                    if user_ == 1:
                        print('home page')
                    else:                
                        print('can not provide change or no balance')
                    break
            elif opt_ ==2:
                deposite_m = int(input('enter the money you want to deposite: '))
                if deposite_m % 100 == 0:
                    AXIS_bank_kumith['balance'] += deposite_m
                    print(f'you have deposited {deposite_m} and the total balance amount: ')
                    break
                else:
                    print('change can not be deposite')
                    break
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


