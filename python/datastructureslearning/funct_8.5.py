"recursive functions"
# def rec_demo(num):
#     if (num>=3):
#         return
    
#     print("hello world")
#     rec_demo(num+1)

# rec_demo(0)





"WAP to print table of a number using recursions"
# def table(num, val):
#     if (num>=11):
#         return 
    
#     print(num*val)
#     table(num+1, val)

# value = int(input("enter the number: "))
# table(1, value)






"WAP to print factorial of a number using recursions"
# def fact(num):
#     if (num==0):
#         return 1
#     else:
#         res = num * fact(num-1)
#         return res

# number = int(input("enter the number: "))
# ans = fact(number)
# print(ans)






"lambda functions"
"they are single line anonymous functions which defined by keyword lambda"

# def sqrt(num):
#     print(num*num)

# sqrt(5)

"anonymous"
# key = lambda n : n*n
# print(key(5))




"WAP to find sum of two numbers using lambda function"

# key = lambda a, b : a+b
# print(key(2,3))

# a, b = 2, 3
# print("the sum {} and {} is {}".format(a, b, key(a, b)))






"write a program to find max of two numbers using lambda function"

# key = lambda a, b : max(a,b)
# a, b = 2, 3
# print("the max of {} and {} is {}".format(a,b, key(a,b)))






"filter function"
"these are first class functions which take another function as an argument"
"selects value on the basis of bool function"
"filter(function, sequence)"

"examples"

# def isEven(num):
#     return (num%2==0)

# l = [1,2,3,4,5,6]
# even_list = list(filter(isEven, l))
# print(even_list)



# def greaterthanThree(num):
#     return (num>3)

# l = [1,2,3,4,5]
# new_list = list(filter(greaterthanThree, l))
# print(new_list)







"Multi-Condition Predicate Generator"
# def dynamic_filter(iterable, *conditions):
#     result=[]
    
#     for item in iterable:
#         is_vaild = True

#         for cond in conditions:
#             if not cond(item):
#                 is_vaild = False
#                 break

#         if is_vaild:
#             result.append(item)

#     return result

# numbers = [1,2,3,4,5,6,7,8]

# filtered_output = dynamic_filter(numbers, lambda x : x%2==0, lambda x : x>3)
# print(filtered_output)





"map function"
"these are also first class functions but instead of depending on bool fns"
"they can take other functions as arguments"
# def double(x):
#     return x*2

# l = [1,2,3,4]
# l1 = list(map(double, l))
# print(l1)


"using lambda functions"
# l = [1,2,3,4]
# l1 = list(map(lambda x: x*2, l))
# print(l1)


"we can use map on multiple sequences"
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# l3 = list(map(lambda x, y: x*y, l1, l2))
# print(l3)






"reduce function"
"first class function that reduces a sequence to a single value"
# from functools import reduce
# def mult(x, y):
#     print(f"value : {x} {y}")
#     return x*y

# l1 = [2,3,5,6]
# ans = reduce(mult, l1)
# print(ans)


"using lambda functions"
# from functools import reduce
# l1 = [2,3,5,6]
# ans = reduce(lambda x, y: x*y, l1)
# print(ans)






"nested functions"
# def func():
#     def inner(x,y):
#         print(f"the sum is {x+y}")
#         print(f"the product is {x*y}")
#     inner(10,20)

# func()
"automatically calls inner"


"calling inner without func()"
# def func():
#     def inner(x,y):
#         print(f"the sum is {x+y}")
#         print(f"the product is {x*y}")
#     return inner

# i1 = func()
# i1(10,20)



