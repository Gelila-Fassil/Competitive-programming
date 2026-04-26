class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # Extra 0 at the end to flush the stack
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                # Update height: increment if '1', else reset to 0
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Solve Largest Rectangle in Histogram for the current row
            stack = [-1]
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area