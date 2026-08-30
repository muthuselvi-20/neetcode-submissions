class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        l1 = len(s)
        l2 = len(t)
        while i < l1 and j < l2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return l2-j