class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for i in details:
            tens = ord(i[11]) - ord("0")
            ones = ord(i[12]) - ord("0")
            age = tens * 10 + ones
            if age > 60:
                result += 1

        return result

