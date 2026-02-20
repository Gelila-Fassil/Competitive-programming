class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                res.append(curr_path[:])
                return
            
            for num in nums:
                if num not in curr_path:
                    curr_path.append(num)
                    backtrack(curr_path)
                    curr_path.pop()
                    
        backtrack([])
        return res