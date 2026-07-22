"in python, functions and their parameters are dynamically typed"

# def fact(x):
#     "this function returns the factorial of an integer"

#     return x

"this returns the doc or the comment placed inside the function"
# print(fact.__doc__)





"multi-line doc"
# def fact(x):
#     """factorial 
#     is returned
#     by this function
#     of any integer"""

#     return x

# print(fact.__doc__)




"positional arguments"
"they require proper positioning during the time of calling the function"

# def showdetail(id, name, dep):
#     print("id: ", id)
#     print("name: ", name)
#     print("department: ", dep)
# showdetail(123, "yash", "cs")

"if positioning is not correct while calling, we reach a wrong output"
# showdetail("yash", 123, "cs")



"keyword argument"
"while calling the function, we specify the keyword and positioning is done automatically"
# showdetail(name="yash", dep="cs", id=123)




"variable length arguments"
"used when multiple arguments are required in a function and their number is not fixed"
# def calculate(*vars):
#     total = 0
#     for val in vars:
#         total+=val

#     print(total)
#     print(type(vars))

# calculate(10)
# calculate(10,20)
# calculate(10,20,30)
# calculate(10,20,30,40)

"its drawback is that it works only for single object"






"keyword variable length arguments (kwargs)"
"advanced version of vars where arguments are stored in key-value pair"
# def greet(**kwargs):
#     print("welcome ", kwargs['name'], " your role is ", kwargs['role'])
#     print(f"Welcome {kwargs['name']}! your role is {kwargs['role']}")
#     print(type(kwargs))

# greet(name = "yash", role = "admin")



# def display(**n):
#     print("record information")
#     for k, v in n.items():
#         print(k, v)

# display(name="yash", marks=100, status="pass")


# def student_report(**n):
#     print("report")
#     for k, v in n.items():
#         print(f"{k}: {v}")

# student_report(name="yash", marks="90", attendance="60")



