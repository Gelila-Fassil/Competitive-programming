class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        res=[]
        res.append(row)
        for i in range (numRows-1):
            next_row = [0] * (len(row)+1)
            for j in range (len(row)):
                next_row[j] = next_row[j] + row[j]
                next_row[j+1] = next_row[j+1] + row[j]
            res.append(next_row)
            row = next_row
        return res


        