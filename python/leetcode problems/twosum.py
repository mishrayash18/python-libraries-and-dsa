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
