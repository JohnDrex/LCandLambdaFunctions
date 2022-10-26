import numbers


def testfunc(num):
    return lambda x: x * num

result10 = testfunc(10)
result100 = testfunc(100)

#alternate method to do the same thing as lines 1 and 2
result10 = lambda x: x*10
result100 = lambda x: x*100

print(result10(9))
print(result100(9))

#filtering a list in order to get only certain numbers that meet a criteria
numbers_list = [2,6,8,10,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)


mapped_list = list(map(lambda num: num % 2, numbers_list))

print(mapped_list)


x = lambda a : a + 10
print(x(5))
