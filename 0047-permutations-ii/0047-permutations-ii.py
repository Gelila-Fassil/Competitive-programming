class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                res.append(curr_path[:])
                return
            
            for i in range(len(nums)):
            
                if used[i]:
                    continue
                
             
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                curr_path.append(nums[i])
                backtrack(curr_path)
                
               
                used[i] = False
                curr_path.pop()
                
        backtrack([])
        return res