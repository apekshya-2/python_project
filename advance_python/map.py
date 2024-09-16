# map() function
# a map() function returns a map object( which is an iterator) of the results after applying the given function to each item of a gicen iterable(list,tuple)
# syntax
# map(fun,iter)
# fun--> function to which map passes each element of given iterable.
# iter--> iterable which is to be mapped
# note: you can pass one or more iterable to the map() function


# to demonstrate working of map
# return double of n
def addition(n):
    return n+n

# we double all numbers using map()
number=(1,2,3,4)
result=map(addition,number)
# addition(1)+1=2
# addition(2)+2=4
# addition(3)+3=6
# addition(4)+4=8
print(list(result))


# lambda Expressions

# double all numbers using map and lambda
numbers=(1,2,3,4)
result=map(lambda x:x+x,numbers)
print(list(result))

# add two list numbers using map and lambda
numbers1=(1,2,3,4,5)
numbers2=(6,7,8,9,10)
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))


# modify the string using map()
# list of strings
l=['apeksha','dhungana','nisha','dhungana']

# map() can listify the list of strings individually
test=list(map(list,l))
print(test)

# if statement with map()
#  using double_even() function 
# define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
    if num % 2 ==0:
        return num*2
    else:
        return  num
    
    # create a list of numbers to apply the function to 
    numbers=[1,2,3,4,5]

    # use map to apply the function to each element in the list
    result=list(map(double_even,numbers))

    # print the result
    print(result)
