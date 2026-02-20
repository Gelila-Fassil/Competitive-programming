class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit_prod = int(num1[i]) * int(num2[j])
                current_sum = digit_prod + res[i + j + 1]
                
                res[i + j + 1] = current_sum % 10
                res[i + j] += current_sum // 10
                
        start_index = 0
        while start_index < len(res) and res[start_index] == 0:
            start_index += 1
            
        return "".join(map(str, res[start_index:]))