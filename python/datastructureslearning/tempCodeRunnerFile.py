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
