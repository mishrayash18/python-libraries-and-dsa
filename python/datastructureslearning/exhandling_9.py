"logical errors are refered to as exceptions"

# print("hello-1")
# print("hello-2")
# print("hello-3")
# print(10/0)
# print("hello-4")
# print("hello-5")
# print("hello-6")

"this gives as abnormal end to the program"



"using try-except blocks we get a normal end to any runtime exception"
# try:
#     print("hello-1")
#     print("hello-2")
#     print("hello-3")
#     print(10/0)
#     print("hello-4")
#     print("hello-5")
#     print("hello-6")
# except ZeroDivisionError as e:
#     print("ERROR! don't divide by zero")

# print("end of program")

"this creates anomaly because after catching the exception, the rest of the"
"code is not executed from the try block"



"to avoid this, in the try block, we should keep only that piece of code"
"that has a possibiliy of giving a runtime error"

# print("hello-1")
# print("hello-2")
# print("hello-3")
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("ERROR! don't divide by zero")
# print("hello-4")
# print("hello-5")
# print("hello-6")
# print("end of program")
"also, one try block can have multiple exception blocks"



"using else block in exception handling"

# print("hello-1")
# print("hello-2")
# print("hello-3")
# try:
#     print(10/1)
# except ZeroDivisionError as e:
#     print("ERROR! don't divide by zero")
# else:
#     print("no exception found")
# print("hello-4")
# print("hello-5")
# print("hello-6")
# print("end of program")





"default exception handler"

# print("hello world")
# try:
#     print(10/0)
# except:
#     print("exception handled")
# print("end of program")

"except is the default excption handler which does not require exception type"

"except block can also handle more than one type of exceptions"

# print("hello world")
# try:
#     print(10/0)
# except(ArithmeticError, TypeError) as e:
#     print("exception handled")
# print("end of program")





"finally blocks"
"executes regardless of the exception"
# print("start")
# n = int(input("enter a number: "))
# try:
#     print(10/n)
    
# except:
#     print("error occurred")

# finally:
#     print("executed successfully")
#     print("end of program")





"raise keyword"
"used for raising user defined or predefined exceptions"
class invalidAgeException(Exception):
    pass

def ageCheck(age):
    if (age<0):
        raise invalidAgeException("only positive intgers allowed")
    if (age>18):
        print("valid to vote")
    else:
        print("invalid to vote")

try:
    n = int(input("enter the age: "))
    ageCheck(n)
except invalidAgeException as e:
    print("error: ", e)
finally:
    print("end of program")






# class TooYoungException(Exception):
#     pass
# class TooOldException(Exception):
#     pass
# class InvalidAgeException(Exception):
#     pass

# def CheckAge(age):
#     if age<0:
#         raise InvalidAgeException("age must be a positive integer")
#     if age<18:
#         raise TooYoungException("wait for 18 to vote")
#     if age>70:
#         raise TooOldException("voting age limit reached")
#     else:
#         print("valid to vote")

# try:
#     n = int(input("enter the age: "))
#     CheckAge(n)
# except(InvalidAgeException, TooYoungException, TooOldException) as e:
#     print("error: ", e)
# finally:
#     print("end of program")