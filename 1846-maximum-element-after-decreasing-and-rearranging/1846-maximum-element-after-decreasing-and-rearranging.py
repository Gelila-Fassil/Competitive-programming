class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr_max = 1
        for i in range (1 , len(arr)):
            if arr[i] > curr_max:
                curr_max +=1
        return curr_max