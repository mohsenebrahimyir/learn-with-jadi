## Yield Functions

# exp (1): simple function
# def firstn():
#     return(1, 2, 3)
# print(firstn())

# exp (2): yield function
# def firstn():
#     yield 1
#     yield 2
#     yield 3
# for i in firstn():
#     print(i)

# exp(3): yield function in loop
# def firstn(n):
#     num = 0
#     while (num<n):
#         yield num
#         num += 1
#
# for i in firstn(10):
#     print(i)