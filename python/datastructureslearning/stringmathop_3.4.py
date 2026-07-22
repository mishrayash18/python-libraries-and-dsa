"slicing"

s = "hellopython"
# print(s[0:10:2])
"start:end:step"
"slice steps cant be 0"

# print(s[:])

# print(s[-1:-10])
"produces an empty slice because the default step is positive"
"the positive step only moves right"
"if start is to the right of the stop, the result is empty"

# print(s[-1:-10:-1])
"slicing backwards with a negative step"

# print(s[::-1])
"reversing the whole string"



"WAP to take input of main string and substr and check"
"if the substr exists in the main string or not"

# s = str(input("enter the string: "))
# substr = str(input("enter the substring: "))
# if (substr in s):
#     print("substr exists")
# else:
#     print("substr does not exist")





"WAP to remove duplicate characters from a string"

# s = (input("enter a string with duplicates: "))
# seen = ""
# result = ""
# for char in s:
#     if char not in seen:
#         result+=char
#         seen+=char
# print("string after removing dups is: ", result)






"WAP to get the number of times each character is present in a str"

# s = (input("enter a string: "))
# seen = ""
# snew = ""
# for char in s:
#     if char not in seen:
#         snew+=char
#         seen+=char



# for char1 in snew:
#     count=0
#     for char2 in s:
#         if char1 == char2:
#             count+=1
#     print(char1, ":", count)

"---count in built function can also be used---"

# for char1 in snew:
#     count = s.count(char1)
#     print(char1, ":", count)






"WAP to reverse a string from spaces"

# s = input("enter a string with spaces: ")
# words = s.split() #splits on whitespace
# reversed_words = words[::-1]
# result = " ".join(reversed_words)
# print(result)



    
    

# WAP to extract all the email addresses in a given text string
# text = "For help, email support@example.com or sales@example.org; you can also CC admin@company.co.uk for urgent requests."
# words = text.split()
# for word in words:
#     clean = word.strip(".,;:")
#     if "@" in word:
#         print(word)












"mathematical operations"
"+ is used as concatenation"
"* is used as repetetion"

# str1 = "hello"+"python"
# print(str1)

# str2 = "hello"*5
# print (str2)