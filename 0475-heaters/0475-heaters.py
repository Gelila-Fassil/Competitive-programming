class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0
        i = 0

        for houses in houses:
            while i+1 < len(heaters) and abs(heaters[i+1] - houses) <= abs(heaters[i] - houses):
                i+=1
            current_dist = abs(heaters[i] - houses)
            radius = max(radius , current_dist)
        return radius
        