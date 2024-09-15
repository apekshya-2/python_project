# to demonstrate working of reduce()
# importing functools for reduce()
import functools

# initializing list
list=[1,3,5,6,2,7]

# using reduce to compute sum of list
print("The sum of the list elements is:", end="")
print(functools.reduce(lambda a,b:a+b,list))

# using reduce to compute maximum element from list
print("The maximum element of the list is:",end="")
print(functools.reduce(lambda a, b: a if a>b else b, list))


# using operator functions
import operator

# list
list=[1,3,5,6,2,7]

# using reducce to compute sum of list
# using operator functions
print("The sum of the list elements is:",end="")
print(functools.reduce(operator.add,list))

# using reducce to compute mul of list
# using operator functions
print("The multiple of the list elements is:",end="")
print(functools.reduce(operator.mul,list))

# using reducce to concatenate string
# using operator functions
print("The concatenated product is:",end="")
print(functools.reduce(operator.add,["apeksha","Dhungana","Dipika"]))

# reduce() vs accumulate()
# both used to calculate the summation of a sequence elements
# reduce()--> "functools" module(store the intermediate result and only returns the final summation value)
#  reduce(function as 1st,sequence as 2nd )
#accumulate()-->"itertools" module(returns a iterator containing the intermediate results, last  number of the iterator returned is summation value of the list)
# accumulate(sequence as 1st,function as 2nd)

# importing itertools for accumulate()
import itertools

# importing functionaltools for reduce()
import functools

# initializing list
list=[1,3,4,10,4,11]

# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print((itertools.accumulate(list, lambda x, y: x+y)))

# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, list))


# reduce() function with three parameters
# to illustrate sum of two numbers
def reduce(function, iterable,initializer=None):
    it=iter(iterable)
    if initializer is None:
        value=next(it)
    else:
        value=initializer
        for element in it:
            value=function(value,element)
            return value
        
        # Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = (2,1,1,2,2,1,1,2)
print(reduce(lambda x, y: x+y, tup,6))








