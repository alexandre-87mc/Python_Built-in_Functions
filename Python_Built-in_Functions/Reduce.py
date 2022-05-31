#Uses function in all items from a list, untill we have 1 element
from functools import reduce

#Using lambda function to sum
list1 = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y: x+y, list1))


#Using commom def for sum
def soma(i,j):
    return i+j
print(reduce(soma,list1))

#Using reduce to find greater number
max_find = lambda a,b: a if (a>b) else b
print(reduce(max_find, list1))