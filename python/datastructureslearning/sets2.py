"mathematical operations on sets"
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}


"union"
"everything in both sets"
# s3 = s1.union(s2)
# print(s3)


"intersection"
"everything common in both sets"
# s3 = s1.intersection(s2)
# print(s3)


"difference"
"items in A but not in B"
# s3 = s1.difference(s2)
# print(s3)


"symmetric difference"
"items in A or B, but not in both"
# s3 = s1.symmetric_difference(s2)
# print(s3)






"relationships between two sets"
s1 = {1,2}
s2 = {1,2,3,4}


"isdisjoint"
# print(s1.isdisjoint(s2))
# print(s1.isdisjoint({5,6}))
"prints true if two sets have no items in common"


"issubset"
# print(s1.issubset(s2))
"prints true if one set is the subset of another"


"issuperset"
# print(s2.issuperset(s1))
"prints true if one set is the superset of another"







"frozen set"
# s = frozenset([1,2,3,4])
# "immutable like a tuple"
# print(s)
# for num in s:
#     print(num)





"WAP to count the number of vowels in a string using sets"
# vowels = {"a", "e", "i", "o", "u"}
# s = input("enter a string: ")
# count = 0
# for char in s:
#     if char in vowels:
#         count+=1
# print(count)