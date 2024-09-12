# lambda , an anonymous functions means that a function is without a name.
# syntax: lambda arguments:expression
calculation=lambda num:"Even number" if num %2==0 else "odd number"
print (calculation(20))


# passed various types of arguments into the different lambda function & printed the result generated from the lambda functions calls
numbers=lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("numbers():",
numbers("code123"))

chain=lambda s: s+ '!'
print("chain():", chain("I am tired"))

find_sum=lambda n: sum([int(x) for x in str(n)])
print("find_sum():",find_sum(103))

# difference between lambda and normal function call
def cube(y):
    print(f"finding cube of number:{y}")
    return y*y*y

lambda_cube=lambda num: num**3
# simple function
print("invoking function defined with def keyword:")
print(cube(30))

# lambda function
print("invoking lambda function:",
      lambda_cube(30))


# use lambda function inside map(),filter(),sorted() and many other functions
a=["1","2","9","0","-1","-2"]
# sort list using sorted()
print("sorted numerically:",
      sorted(a, key=lambda x: int(x)))

# filter() and lambda function
print("filtered positive even numbers:",
      list(filter(lambda x: not (int(x)%2==0 and int(x)>0),a)))

# casting to int, then convert items to string again
print("operation on each item using lambda and map()",
      list(map(lambda x: str(int(x)+10),a)))
