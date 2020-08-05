# def tri_recursion(k):
#     print(k)
#     if (k > 0):
#         result = k + tri_recursion(k - 3)
#         #print(result)
#     else:
#         result = 0

#     print(k, result)
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(9)



            #FACTORIAL

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an angle"""

#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 8
# print("The factorial of", num, "is", factorial(num))



_list = [3,4,8,22,34,54,60]

def moving_differece(_list, differences = []):

    if len(_list) < 2:
        return differences
    else:
        differences.append(_list[1] - _list[0])
        return moving_differece(_list[1:], differences)

print(moving_differece(_list))
