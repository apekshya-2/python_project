#1.list comprehension
numbers=[11,12,13,]
doubled=[x*2 for x in numbers]
print(doubled)
# newlist=[expression(element) for elment in oldlist if condition]

numbers=[1,2,3,4,5,6]
squared=[x**2 for x in numbers]
print(squared)

# 2. Iteration with List Comprehension
# using list comprehension to iterate through loop
list=[character for character in [1,2,3,4]]
print(list)

# 3. even list using list comprehension
list=[i for i in range(12) if i % 2==0]
print(list)

#4. matrix using list comprehension
matrix=[[j for j in range(3)] for i in range(3)]
print(matrix)

# 5. list comprehensions vs for loop
list=[] 
for character in 'I am apekshya !':
    list.append(character)

    print(list)

# 6.time analysis in list comprehensions and loop
import time
# define function to implement for loop
def for_loop(n):
    result=[]
    for i in range(n):
        result.append(i**2)
        return result
    # define function to implement list comprehension
    def list_comprehension(n):
        return[i**2 for i in range(n)]
    
    #calculate time taken by for_loop()
    start=time.time()
    for_loop(10**6)
    end= time.time()

    #display time taken by for_loop()
    print('time taken for_loop:', round(end-start,2))

    # calculate time takens by list_comprehension()
    start=time.time()
    list_comprehension(10**6)
    end=time.time()

    # display time taken by for_loop()
    print('time taken for list_comprehension:', round(end-start,2))

    # nested list comprehensions
    matrix=[]
    for i in range(3):
        # append an empty sublist inside the list
        matrix.append([])

        for j in range (5):
            matrix[i].append(j)

            print(matrix)

            # list comprehensions and lambda
            number=[]
            for i in range(1,7):
                number.append(i*10)
                print(number)

                # using lambda to print table of 10
                numbers= list(map(lambda i:i*10,[i for i in range(1,6)]))
                print(numbers)

                # display transpose of 2d-matrix
                #assign matrix
                twoDmatrix=[[10,20,30],
                            [40,50,60],
                            [70,80,90]]
                # transpose
                trans=[[i[j] for i in twoDmatrix] for j in range(len(twoDmatrix[0]))]
                print(trans)

                # toggle the case of each character in a string
                # initializing string
                string='i am apekshya'
                # toggle case of each character
                list=list(map(lambda i: chr(ord(i)^32), string))
                print(list)
    
    

