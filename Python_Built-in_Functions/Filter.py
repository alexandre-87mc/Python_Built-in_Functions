#Filter method allows filter every element in a list
list1 = [1,2,3,4,5,6,7,8,9,10]

#Create a list of pairs
print(list(filter(lambda x: x%2==0, list1)))