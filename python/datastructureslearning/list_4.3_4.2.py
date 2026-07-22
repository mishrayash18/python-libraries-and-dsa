"list comprehension and one line comprehension"

"WAP to store the squares of the first 10 n in a list"
"normal method"
# item = []
# for val in range(1,11):
#     item.append(val*val)
# print(item)


"comprehension method"
"“Comprehension” means the ability to understand something fully"
# item = [val*val for val in range(1,11)]
# print(item)

"comprehension with condition"
# item = [val*val for val in range(1,11) if val%2==0]
# print(item)


# words = ["abc", "abcd", "pqrstu", "xyz"]
# item = [word for word in words if len(word)>5]
# print(item)



"intersection of two lists using comprehensions"
# l1 = [10,20,30,40,50]
# l2 = [30,40,50,60,70]
# item = [x for x in l1 if x in l2]
# print(item)







"traversing in a list"

"while loop"
# items = [10,20,30,40]
# idx=0
# while idx < len(items):
#     print(items[idx])
#     idx+=1


"for loop"
# items = [10,20,30,40]
# for num in items:
#     print(num)







"methods of a list"
"len and count"

"WAP to find the index of an element of a list"

# l = [10,20,30,40,50]
# num = int(input("enter the nmber: "))

# if l.count(num)>0:
#     print(l.index(num))
# else:
#     print("not in list")




"append and insert"
"append -> push at the end of the list"
"insert -> specify the position to insert"

# l = [10,20,30,40,50]
# l.append(60)
# l.insert(1, 80)
# print(l)