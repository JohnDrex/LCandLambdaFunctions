''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_even = list(filter(lambda num: (num % 2== 0), numbers_list))
print(filtered_even)


filtered_odd = list(filter(lambda num: (num % 2 ==1), numbers_list))
print(filtered_odd)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_list = list(filter(lambda x: (len(x) ==6), weekdays))
print(day_list)

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
'''

oglist = ['orange', 'red', 'green', 'blue', 'white', 'black']
removelist = ['orange', 'black']
filtered_list = list(filter(lambda word: (word not in removelist ), oglist))
#filtered_list = list(filter(lambda word: (word != 'black'), filtered_list))

print(filtered_list)


''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

filtered_list = list(filter(lambda num: (num not in list2), list1))

print(filtered_list)

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
listword = ['red', 'black', 'white', 'green', 'orange']
letters = 'ack'
filtered_list = list(filter(lambda word: ('ack' in word in listword), listword))
print(filtered_list)
filtered_list = list(filter(lambda word: ('abc' in word in listword), listword))
print(filtered_list)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"
list1=["Hello8world","HELLO", "hello"]

mapped_list = list(map(lambda x: (len(x) >=8) , list1))


print(mapped_list)




''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key = lambda score: score[1])
print(original_scores)