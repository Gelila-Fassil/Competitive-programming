class Solution:
    def isValid(self, s: str) -> bool:
        sign_map = {")":"(" , "}":"{" , "]":"["}
        stack =[]

        for char in s:
            if char in sign_map:
                topElement = stack.pop() if stack else '#'
                if sign_map[char] != topElement:
                    return False
            else:
                stack.append(char)
        return not stack