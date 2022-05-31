#Enumerate

list1 = ['a','b','c','d']
count = 0

#print list
for l in list1:
    print(l)

#Print and enumerate list
for l in list1:
    print(count, ':', l)
    count += 1

#Using Enumerate
for number,item in enumerate(list1):
    print(number, ':', item)

test_enumerate = enumerate(list1)
print(list(test_enumerate))