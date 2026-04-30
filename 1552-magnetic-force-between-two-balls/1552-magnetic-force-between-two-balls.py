class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def can_place(mid):
            count = 1 
            last_pos = position[0]
            
            for i in range(1, n):
                if position[i] - last_pos >= mid:
                    count += 1
                    last_pos = position[i]
                if count >= m:
                    return True
            return False
        low = 1
        high = position[-1] - position[0]
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                res = mid 
                low = mid + 1
            else:
                high = mid - 1
                
        return res