class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_index = [1]

        for i in range (rowIndex):
            next_row =[0] * (len(row_index) +1)
            for j in range(len(row_index)):
                next_row[j] = next_row[j] + row_index[j]
                next_row[j+1] = next_row[j+1] + row_index[j]
            row_index = next_row
                

        return row_index














  
        










