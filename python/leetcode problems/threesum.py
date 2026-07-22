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
