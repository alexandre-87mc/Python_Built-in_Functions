#1 - Use map() to build a function that finds the lenght
#of every word in the string, and returns a list
st1 = 'How long are the words in this phrase'
def word_lenghts(string_x):
    print(list(map(len,string_x.split())))
word_lenghts(st1)

#2 - Use reduce() to take a list of digits and return
#the number they correspond. Don't convert int to string!
#digits_to_num([1,2,3,4,5])
#12345
from functools import reduce
number_list_1 = [1,2,3,4,5,6,7,8,9,0]
sum_base_10 = lambda x,y: 10*x + y
def digits_to_num(list_num):
    print(reduce(sum_base_10,list_num))
digits_to_num(number_list_1)

#3 - Use filter to return the words from a list that
#starts with a especific letter
#l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
#filter_words(l,'h')
l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
def Print_string(s1):
    if s1[0]=='h':
        print(s1) 
def Filter_first_letter(list2):
    list(filter(Print_string, list2))
Filter_first_letter(l)

#4 - Use zip and list comprehension to return a list the same size where
#each value is equal to 2 values from the characteres from L1 and L2
#concatenateds together with the conector between then
#concatenate(['A','B'],['a','b'],'-')
#['A-a', 'B-b']
l1 = ['a','b','c']
l2 = ['A','B','C']
def concatenate_words(L1, L2, connector):
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]
print(concatenate_words(l1, l2, '-'))

#5 - Use enumerate with other methods to return a dictionarie that has the values
#of list as keys and the index as value. You can assume a value only appears once in the list
#d_list(['a', 'b', 'c'])
#{'a':0, 'b':1, 'c':2}
def Create_dictionaries(list6):
    in_list1 = enumerate(list6)
    return dict(in_list1)
list_pre_dict = ['a','b','c']
dictio1 = Create_dictionaries(list_pre_dict)
print(dictio1)

#6 - Use enumerate with other methods to return the number of items 
#in the list tha has value equal to your index
#count_match_index([0,2,2,1,5,5,6,10])
L = [0,2,2,1,5,5,6,10]
def count_MIndex(L):
    return len([num for count,num in enumerate(L) if num == count])