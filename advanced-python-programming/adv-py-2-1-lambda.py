## Lambda Function Structure

# exp (1): Define lambda function without name
# lambda x: x*2

# exp (2): Define lambda function with 'myfunc' name
# myfunc = lambda x: x*2
# print(myfunc(3))

## Use lambda for sort a tuple list

# a = [(3, 4), (7, 1), (5, 9), (2, 2)]
# print(a)

# exp (1): Sort by first value in tuple
# a.sort()
# print(a)

# exp (2): Sort by second value in tuple
# a.sort(key= lambda x:x[1])
# print(a)

## Use lambda in Map for list 

# exp (1): x times 2
# mylist = [1, 2, 4, 2, 0.8]
# newlist = map(lambda x:x*2, mylist)
# print(newlist)
# newlist = list(newlist)
# print(newlist)

# exp (2): replace 'big' for x greater than 10 and else 'small'
# numbers = [10, 11, 8, 6, 100, 7, 9, 12]
# big_small = map(lambda x: 'big' if x>10 else 'small', numbers)
# big_small = list(big_small)
# print(big_small)

## Use lambda in filter

# exp (1): Filter even numbers
# my_list = [1, 5, 6, 8, 10, 11]
# filter_even = filter(lambda x: x % 2 == 0, my_list)
# filter_even = list(filter_even)
# print(filter_even)