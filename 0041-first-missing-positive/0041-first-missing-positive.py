# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         nums.sort()
#         result = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 result.append(nums[i])
#         for i in range (len(result)+1):
#             positiveNum = i + 1
#             if positiveNum in result:
#                 continue
#             else:
#                 return positiveNum
                
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
           
            
        