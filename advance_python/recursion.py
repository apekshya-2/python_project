
# recursion can be defined as the process of defining something in terms of itself
# it is a process in which a function calls itself directly or indirectly

# syntax:
# def func():<--||(recursive call)|   func()----


# A fibonacci sequence is the integer sequence
# recursive function
def recursive_fibonacci(n):
    if n <=1:
        return n
    else:
        return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2))
    
    n_terms=10

    # check if the number of terms is valid
    if n_terms <=0:
        print("Invalid input ! Please input a positive value")
    else:
        print("Fibonacci series:")
        for i in range(n_terms):
            print(recursive_fibonacci(i))


# the factorial of 6 is denoted as 6!
# program to print factorial of a number recursively
# recursive function
# def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)
    

    # user input
    num=6

    # check if the input is valid or not
    if num<0:
        print("Invalid input ! please enter a positive number.")
    elif num==0:
        print("Factorial of number 0 is 1")
    else:
        print("factorial of number",num,"=",recursive_factorial(num))
    

    # tail recursion
    # a unique type of recursion where the last procedure of a function is a recursive call.
    #  optimized by the compiler which makes it better than non-tail recursive functions

    # program to calculate factorial of a number 
    # using a non- tail recursive function

    # non tail recursion function
    def recur_facto(n):
        if(n==0):
            return 1
        return n* recur_facto(n-1)
    
    # print the result
    print(recur_facto(6))



    # program to calculate factorial of a number
    # using a tail recursive function
    # a tail recursive function
    def recur_facto(n,a=1):
        if(n==0):
            return a
        return recur_facto(n-1,n*a)
    
    # print the result
    print(recur_facto(6))