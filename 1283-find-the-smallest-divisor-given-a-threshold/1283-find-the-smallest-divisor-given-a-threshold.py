import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        answer = high
        while low <= high:
            mid = (low + high) //2
            current_sum = 0
            for i in nums:
                current_sum += (i + mid -1)//mid
            if current_sum  <= threshold:
                    answer = mid
                    high = mid-1
            else:
                 low = mid +1
                        
        return answer
        