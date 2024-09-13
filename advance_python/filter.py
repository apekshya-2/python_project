# python filter() Syntax
# filter(function,sequence)
#  function that tests if each element of a sequence is true or not
#  sequence which needs to be filtereed, it can be sets,lits, tuples or containers of any iterators


# python filter function with a custom function
# fun() to filter out vowels from the python list
# function that filters vowels
def fun(variable):
    letters=['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
    
# sequence
sequence=['b','g','e','e','j','k','s','p','r']

# using filter function
filtered=filter(fun,sequence)

print('the filtered letters are:')
for s in filtered:
    print(s)

# filter function in python with lambda
# a list contains both even and odd numbers
sequence=[0,1,2,3,5,8,13,14,15]

# result contains odd numbers of the list
result=filter(lambda x:x%2 !=0,sequence)
print(list(result))

# result contains even numbers of the list
result=filter(lambda x: x%2 ==0,sequence)
print(list(result))

# filter function in python with lambda and custom function
# define a function to check
# if a number is a multiple of 4
def is_multiple_of_4(num):
    return num%4==0

# create a list of number to filter
number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# use filter and a lambda function to 
# filter the list of number and only
# keep the ones that are multiples of 4
result=list(filter(lambda x: is_multiple_of_4(x),number))

# print the result
print(result)
