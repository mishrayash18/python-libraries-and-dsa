"this library introduces type hinting in python"

"typehinting variables, functions and datastructures"

"typehinting is used only for developer reference and tool reference"
"they are completely ignored while running the code"

# name : str = "yash"
# age: int = 20
# score: float = 9.2
# l1 : list[str] = ["a", "b", "c"]

# def greet(name:str, age:int, score: float, l1: list[str]) -> str:
#     return f"hello {name}, your age is {age} and score is {score} and list is {l1}"

# newG = greet(name, age, score, l1)
# print(newG)




# def countguests(guestlist: list[str]) -> int:
#     return len(guestlist)

# guestlist:list[int] = ["a","b","c"]
"typehinting is wrong still we dont get an error"
# count = countguests(guestlist)
# print(count)



# from typing import Union
"union feature of typehingting is used when we want to give"
"typehinting for more than one datatypes for a single object"
# def userID(id: Union[str, int]) -> Union[str, int]:
#      return f"the user id is {id}"

# print(userID(123))
# print(userID("A-101"))




"any is a feature that refers to as typehinting any datatype being stored"
"used for highly unpredictable outputs"
# from typing import Any
# def show(a:any) -> any:
#     return a
# print(show(123))
# print(show("hello"))
# print(show(4.5))




"callable feature is used to typehint a function"
# from typing import Callable
# def calculate(a:int, b:int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)

# def add(a:int, b:int)->int:
#     return f"the addition is {a+b}"

# def sub(a:int, b:int)->int:
#     return f"the subtraction is {a-b}"

# def multiply(a:int, b:int)->int:
#     return f"themuliplication is {a*b}"

# print(calculate(6,5,add))
# print(calculate(6,5,sub))
# print(calculate(6,5,multiply))




"optional feature handles missing values as a function might return"
"a datatype profile or none"
# from typing import Optional
# def status(id: int) -> Optional[str]:
#     if (id == 101):
#         return "Active"
    
    
# print(status(102))




"typevar introduces generics in python"
# from typing import TypeVar
# T = TypeVar('T')
# def getfirstitem(items: list[T]) -> T:
#     return items[0]

# l1 = [1,2,3]
# l2 = ["a", "b", "c"]
# print(getfirstitem(l1))
# print(getfirstitem(l2))