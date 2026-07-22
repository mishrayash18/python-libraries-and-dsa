"two sum- brute force"
# def twosum(nums: list[int], target: int) -> list[int]:
    
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):

#             if (nums[i]+nums[j] == target):
#                 return [i,j]


# main = twosum([4,2,6,11,15], 8)
# print(main)               




"two sum- optimized"
# def twosum(nums: list[int], target: int) -> list[int]:
#     seen = {}
#     for i in range(0, len(nums)):

#         if target-nums[i] in seen:
#             return [seen[target-nums[i]], i]
#         else:
#             seen[nums[i]] = i
        
# main = twosum([2,7,11,15], 9)
# print(main)




"valid anagram"
# def isAnagram(s:str, t:str) -> bool:
#     snew = sorted(s)
#     tnew = sorted(t)

#     return (snew == tnew)
    
# main = isAnagram("car", "arc")
# print(main)






"valid palindrome"
# def isPalindrome(s: str) -> bool:
#     snew = []
#     for i in s:
#         if i.isalnum():
#             snew.append(i.lower())

#     return (snew == snew[::-1])

# main = isPalindrome("Racecar:")
# print(main)




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




"3 sum"
# def threesum(numbers:list[int]) -> list[list[int]]:
#     ans = []
#     numbers.sort()
#     for i in range(0, len(numbers)):
#         for j in range(i+1, len(numbers)):
#             for k in range(j+1, len(numbers)):
#                 if (numbers[i]+numbers[j]+numbers[k] == 0):
#                     anspair = []
#                     anspair.append(numbers[i])
#                     anspair.append(numbers[j])
#                     anspair.append(numbers[k])
#                     if anspair not in ans:
#                         ans.append(anspair)

#     return ans

# numberlist = [-1, -2 , 0 , 1, 2, -3, -4, 3, 4]
# print(threesum(numberlist))




"index of the first appearance of a string"
# def strStr(haystack:str, needle:str) -> int:
#     for i in range(0, len(haystack)):
        