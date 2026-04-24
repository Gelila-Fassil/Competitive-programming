import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_start = []
        for i in range(len(intervals)):
            sorted_start.append([intervals[i][0], i])
        sorted_start.sort()
        starts = [x[0] for x in sorted_start]

        result = []
        for interval in intervals:
            end_val = interval[1]
            idx = bisect.bisect_left(starts, end_val)

            if idx < len(sorted_start):
                result.append(sorted_start[idx][1])
            else:
                result.append(-1)
        return result