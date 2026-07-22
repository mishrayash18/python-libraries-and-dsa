"counter - a dictionary subclass designed to count the elements of an iterable"
# from collections import Counter

# mydict = {"a":2, "b":1, "c":4, "d":3}
# mycount = Counter(mydict)
# print(mycount)



# from collections import Counter

# mylist = ['a','a','a','b','b','c','d','d','d']
# mycount = Counter(mylist)
# print(mycount)



"""you are building a casting system for a movie studio. The studio has a script containing a list of character
archetypes needed for a movie. They also have an application pool of actors available for hire. Each actor can
play exactly one specific archetype.Write a function can_cast_movie(script, actors) that determines
if the studio has enough available actors to fill every role in the script"""

# from collections import Counter
# def can_cast_movie(script:list[str], actors:list[str]) -> bool:
#     return not (Counter(script)-Counter(actors))

# actors = ['hero', 'villain', 'villain', 'villain', 'sidekick']
# script = ['hero', 'sidekick']
# print(can_cast_movie(script, actors))





# from collections import Counter
# def can_build_ransom_note(mag:str, note:str) -> bool:
#     mag1 = str()
#     for char in mag:
#         if char!=" ":
#             mag1+=char

#     note1 = str()
#     for char in note:
#         if char!=" ":
#             note1+=char
    
#     return not (Counter(note1)-Counter(mag1))

# print(can_build_ransom_note('a b a c', 'ac'))




# from collections import Counter
# text = 'a b c a b c a a b c a b b'
# counts = Counter(text.split())
# print(counts.most_common(2))



"""defaultdict - a python subclass that creates a dictionary. The standard dictionary crashes when we
try to search or modify a key that does not exist, but the defaultdict creates a new key for that case
and assigns a default value to it"""

"using standard dictionary"
# cities = [("India", "Indore"), ("India", "Mumbai"), ("US", "Chicago")]
# countrymap = {}

# for country, city in cities:
#     if country not in countrymap:
#         countrymap[country] = []
#     countrymap[country].append(city)

# print(countrymap)




"using default dict"
"created empty lists as values for new keys automatically"
# from collections import defaultdict
# cities = [("India", "Indore"), ("India", "Mumbai"), ("US", "Chicago")]
# countrymap = defaultdict(list)

# for country, city in cities:
#     countrymap[country].append(city)

# print(countrymap)



"using sets in defaultdict"
# from collections import defaultdict
# cities = [("India", "Indore"), ("India", "indore"), ("US", "Chicago")]

    
# countrymap = defaultdict(set)

# for country, city in cities:
#     std_country = country.title()
#     std_city = city.title()
#     countrymap[std_country].add(std_city)
# print(countrymap)



"lambda functions in defaultdict"
# from collections import defaultdict
# jobs = defaultdict(lambda:'pending')
# jobs['task1']
# jobs['task2']
# jobs['task3']
# jobs["task1"] = "done"
# print(jobs)



"creating a 2d structure using defaultdict"
# from collections import defaultdict
# matrix = defaultdict(lambda:defaultdict(int))
# matrix['row1']['col1']=5
# matrix['row2']['col1']
# matrix['row3']['col1']
# print(matrix)




"""deque - it is a short form of double ended queues, they are faster than lists as accessing
and modifying a deque takes O(1) time whereas for lists it takes O(n)
but they are not a complete replacement for lists as they do not provide slicing operations"""
# from collections import deque
# struct = deque()
"add operations"
# struct.append('a')
# struct.append('b')
# struct.append('c')
# struct.append('d')
# struct.appendleft('e')

"delete operations"
# struct.pop()
# struct.popleft()

"rotate operations"
# struct.rotate(1)
# struct.rotate(-2)
# print(struct)

"maxlen method"
# log = deque(maxlen=3)
# log.append('entry')
# log.append('register')
# log.append('exit')
# log.append('logout')
# print(log)




"""frequency anagrams - two words are considered frequency anagrams if the frequency of their
letters are same, neglecting if the words are same"""

# from collections import Counter, defaultdict
# list_of_words = ['aabc', 'yxxz', 'abc', 'zxy', 'ab','xy']
# count_of_letters = {}
# word_groups = defaultdict(list)

# for i in list_of_words:
#     count_of_letters[i] = Counter(i)
    
# for k, v in count_of_letters.items():
#     temp1 = []
    
#     for values in v.values():
#         temp1.append(values)

#     temp1.sort()
#     temp1 = tuple(temp1)
#     word_groups[temp1].append(k)     

# print(word_groups)





"""You are given a list of integers. Your goal is to group the numbers together based on how many
times they appear in the dataset, but only if their total appearance count is a prime number.
Any number that appears a non-prime number of times (like 1, 4, 6, 8, etc.)
should be completely ignored"""

# from collections import Counter, defaultdict

# def is_prime(n:int) -> bool:
#     if n<2:
#         return False
    
#     for i in range(2,n):
#         if n%i == 0:
#             return False
    
#     return True

# numbers = [7, 4, 7, 5, 4, 4, 7, 9, 5, 4, 2, 2, 2]
# number_count = Counter(numbers)
# prime_count_dict = defaultdict(list)

# for k, v in number_count.items():
#     if is_prime(v):
#         prime_count_dict[v].append(k)

# print(prime_count_dict)





"""namedtuple - A namedtuple is a factory function in Python's collections module
that creates a subclass of the standard tuple. It allows you to assign names to each
position in a tuple, meaning you can access elements using readable attribute names (dot notation)
instead of error-prone numeric indices"""
# from collections import namedtuple
# Car = namedtuple('Car', 'color type mileage')
# my_car = Car(color='black', type='sedan', mileage='15000')
# print(my_car.color)
# print(my_car.type)
# print(my_car.mileage)


"asdict method"
# print(my_car._asdict())


"create from an iterable ._make()"
# car_data = ['blue', 'SUV', 12000]
# my_car1 = Car._make(car_data)
# print(my_car1)


"typing.namedtuple"
# from typing import NamedTuple
# class User(NamedTuple):
#     id:int
#     username:str
#     password:int

# user1 = User(101, "bunny", 1234)
# print(user1)