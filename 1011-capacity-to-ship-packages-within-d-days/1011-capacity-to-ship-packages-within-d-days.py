class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        capacity = high

        while low <=high:
            mid = (low + high) //2
            days_needed = 1
            current_load = 0

            for w in weights:
                if current_load + w > mid:
                    days_needed +=1
                    current_load = w
                else:
                    current_load +=w
            if days_needed <= days:
                capacity = mid
                high = mid -1
            else:
                low = mid +1
        return capacity

     