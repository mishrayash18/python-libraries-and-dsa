"list, tuple and sets stored single elements as entities"
"dictionaries store key:value pairs as single entities"
"they are mutable"


"traditional way"
# person = {"name":"yash", "age": 20, "uni": "UPES"}
# print(person)


"creating a dictionary from sequence having each value as a pair"
# person = dict([("name", "yash"), ("age", 20), ("uni", "UPES")])
# print(person)


"accessing the elements of a dictionary"
person = {"name":"yash", "age": 20, "uni": "UPES"}

"gives error if key dne"
# print(person["name"])

"safer method as it returns none if key dne"
# print(person.get("name"))


"accessing only keys"
# print(person.keys())


"accessing only values"
# print(person.values())


"accessing all the items"
# print(person.items())


"iterating dictionary using for loop"
# for key in person:
#     print(key, ":", person[key])


"iterating dictionary using items() method"
# for key_value in person.items():
#     print(key_value[0], ":", key_value[1])





"adding items in a dictionary"
"key value assignment"
person["sapID"] = 1234
# print(person)


"update method"
person.update({"status" : "pass"})
# print(person)




"removing operations in a dictionary"
"pop operation"
# person.pop("age")
# print(person)


"popitem operation- removes the last added key:value pair added"
# person.popitem()
# print(person)


"combining two dictionaries"

"using update"
# r = {1:"a", 2:"b", 3:"c"}
# person.update(r)
# print(person)


"using union"
# d1 = {1:"a", 2:"b", 3:"c"}
# d2 = {4:"d", 5:"e"}
# d3 = d1 | d2
# print(d3)


"using in-place operation"
# d1 = {1:"a", 2:"b", 3:"c"}
# d2 = {4:"d", 5:"e"}
# d1 |= d2
"new dictionary is not required"


