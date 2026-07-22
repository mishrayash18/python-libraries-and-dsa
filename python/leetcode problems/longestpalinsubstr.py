"longest palindromic substring"
# def longestPalindrome(word:str) -> str:
#     longest = ""
#     for i in range(0, len(word)):
#         for j in range(i+1, len(word)):
#             substring = word[i:]
            
#             if substring == substring[::-1] and len(substring)>len(longest):
#                 longest = substring
#         if len(word) == 1:
#             return word
#     return longest

# word = "bb"
# print(longestPalindrome(word))