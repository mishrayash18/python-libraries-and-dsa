"nested dictionary"
# info = {"yash":
#         {
#             "ID" : 1234,
#             "age" : 20,
#             "status" : "pass"
#         },
#         "abc":
#         {
#             "ID" : 5,
#             "age" : 20,
#             "status" : ["pass", "/", "fail"]
#         }
#     }
# print (info["abc"]["ID"])
# print(info["abc"]["status"])
# print(info["abc"]["status"][0])


"sorted dictionary"
# sorted_info = sorted(info.items())
# print(sorted_info)


"sorting by keys"
# info = {"c":7, "b":10, "a":9}
# sorted_dict=sorted(info.items())
# print(sorted_dict)


"sorting in reverse order"
# revsorted_dict = sorted(info.items(), reverse = True)
# print(revsorted_dict)


"sorting by values"
# sorted_dict = sorted(info.items(), key = lambda pair : pair[1])
# print(sorted_dict)


"sorting by values in reverse order"
# sorted_dict = sorted(info.items(), key = lambda pair : pair[1], reverse=True)
# print(sorted_dict)


"manage a list of contacts where each contact is "
"represented as a dictionary with fields such as name, phone no and email"

contacts = [
    {"name": "Alice Johnson", "phone": "555-123-4567", "email": "alice.johnson@example.com"},
    {"name": "Bob Martinez", "phone": "555-987-6543", "email": "bob.martinez@example.com"},
    {"name": "Cara Singh", "phone": "555-555-1212", "email": "cara.singh@example.com"},
    {"name": "Daniel Kim", "phone": "555-222-3333", "email": "daniel.kim@example.com"},
    {"name": "Emma Lee", "phone": "555-444-5555", "email": "emma.lee@example.com"},
]

"add operation"
contacts.append({"name":"yash", "phone":"123", "email":"xyz@mail"})

search_name = input("enter the name: ")
for item in contacts:
    if item["name"].lower() == search_name.lower():
        print(item["phone"])
else:
        print("not found")    
