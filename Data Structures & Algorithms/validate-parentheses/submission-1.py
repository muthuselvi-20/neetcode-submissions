class Solution:
    def isValid(self, s: str) -> bool:
        data = {"]":"[",")":"(","}":"{"}
        stack = []
        for i in s:
            if i in data:
                if not stack or stack.pop() != data[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0