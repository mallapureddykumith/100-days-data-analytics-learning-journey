'''
anonymous function
-----------------
-anonymous function is a function that don't any
-this is also called as lambda function
-lambda function will take n number arguements but only one expression

syntax- lambda arguments:expression
ex-so = lambda a,b,c : a+b+c
print(so(2,45,6))

ex.def num(n):
    if n == 1:
        return 1
    return n* num(n-1)
print(num(5))

map()
---------------
the map function will be applied on the given function of each and every element of an itterable
ex-num = [1,2,3,4,5]
so = list(map(lambda x: x*x,num))
print(so)

filter()
---------
-filter() function will only consider if the condition is true, then it will keep that values...
ex-num = [1,2,3,4,5]
so = list(filter(lambda x: x%2 ==0,num))
print(so)

reduce()
=------------
-the reduce function consider all elements and reduce to one single element...
syntax-to use this reduce () we have to import it first from the fnctools
..
ex-num = [1,2,3,4,5]
so = list(filter(lambda x: x%2 ==0,num))
print(so)

print()
----------
-print is an inbuilt function that is used to for  display purpose the values stored by variable

return
-only used inside the functions (any functions)
-when the return is executed then it will exit from that function and holds the returned values in the calling 
'''

from functools import reduce
nums = [1,2,3,4,5]
so = reduce(lambda x,y:x+y,nums)
print(so)


