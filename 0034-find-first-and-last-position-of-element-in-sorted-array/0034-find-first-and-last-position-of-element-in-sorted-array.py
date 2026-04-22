class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums, target, True)
        right = self.binsearch(nums, target, False)
        return [left, right]

    def binsearch(self, nums, target, leftbias):
        low = 0
        high = len(nums) - 1
        i = -1
        
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1 
            elif target < nums[mid]:
                high = mid - 1
            else:
                i = mid 
                if leftbias:
                    high = mid - 1
                else:
                    # Keep looking right to find the VERY last occurrence
                    low = mid + 1
        return i