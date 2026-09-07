class Solution:
    def maxDifference(self, s: str) -> int:
        fre = {}
        for i in s:
            fre[i] = fre.get(i,0) +1
        odd = 0
        even = float("inf")
        for val,count in fre.items():
            if count % 2 == 0:
                even = min(even,count)
            elif count % 2 == 1:
                odd = max(odd,count)
        return odd - even    