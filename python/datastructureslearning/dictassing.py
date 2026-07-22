"WAP to group similar items to dictionary values list"
# test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]

# unique = set(test_list)

# d = {}

# for num in unique:
#     numlist=[]
#     for i in test_list:
#         if (i == num):
#             numlist.append(i)

#     d.update({num : numlist})
# print(d)    






"WAP to convert a list of dictionaries to a list of lists"
# contacts = [
#     {"name": "Alice", "email": "alice@example.com"},
#     {"name": "Bob", "email": "bob@example.com"},
# ]

# rows = [list(d.values()) for d in contacts]
# column = [list(d.keys()) for d in contacts]
# l = []

# l.append(rows)
# l.append(column)
# s = set(l)
# l1 = list(s)

# print(l1)






"WAP to print all the distinct values in a dictionary"
# data = {
#     "apple": "fruit",
#     "banana": "fruit",
#     "carrot": "vegetable",
#     "spinach": "vegetable",
#     "water": "drink"
# }

# s = set(value for value in data.values())
# print(s)



"WAP to find the highest 3 values of corresponding keys in a dictionary"
# data = {"a": 10, "d": 300, "c": 120, "b": 75, "e": 999}

# for i in range(0, 3):
#     key, value = max(data.items(), key= lambda pair : pair[1])
#     print(key)
#     data.pop(key)
     
"simpler method"
# sorted_data = sorted(data.items(), key = lambda pair: pair[1], reverse=True)[:3]
# print(sorted_data)





"WAP to sort a list alphabetically in a dictionary"
# data = {"a":[2,3,1], "b":[5,1,2], "c":[9,5,7]}
# sorted_data = {}
# for key, value in data.items():
#     sorted_data[key] = sorted(value)

# print(sorted_data)