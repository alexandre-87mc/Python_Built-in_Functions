#Zip Agregates 2 variables and return tuple
x = [1,2,3,7,8,9]
y = [4,5,6,10,11,12]
print(list(zip(x,y)))

#print the max value between items
for i in zip(x,y):
    print(max(i))

#Ziping dictionaries
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
print(list(zip(d1,d2.values())))