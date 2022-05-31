#Map uses a function in all items from a list

#Lambda
def fahrenheit(T):
    return (9/5) * T + 32

temp = [9, 22, 40, 90, 120]

for t in temp:
    print(fahrenheit(t))

#Using map
print(list(map(fahrenheit, temp)))


