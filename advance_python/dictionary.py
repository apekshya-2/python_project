# dictionary comprehension
# a dictionary comprehension takes the form{key:value for(key,value) in iterable}

keys=['a','b','c','d','e']
values=[1,2,3,4,5]
mydict={k:v for (k,v) in zip(keys,values)}
print(mydict)

# using fromkeys() method
dic=dict.fromkeys(range(5), true)
print(dic)

# creation using list comprehension
mydict={x:x**2 for x in [1,2,3,4,5]}
print(mydict)

# using conditional statements in dictionary comprehension
mydict={x: x**3 for x in range(10) if x**3%4==0}
print(mydict)

# using nested dictionary comprehension
l="abc"
dic={
    x:{y:x+y for y in l} for x in l
}
print(dic)