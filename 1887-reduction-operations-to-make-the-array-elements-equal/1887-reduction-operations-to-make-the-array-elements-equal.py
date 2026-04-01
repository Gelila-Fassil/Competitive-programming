class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total_ops = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                total_ops += (n - i)
        return total_ops
    

 
        
            
            
    
        















        

        