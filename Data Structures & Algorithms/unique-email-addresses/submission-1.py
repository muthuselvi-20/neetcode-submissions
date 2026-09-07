class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            n,d = i.split("@")
            n = n.split("+")[0]
            n = n.replace(".","")
            c = n+"@"+d
            s.add(c)
        return len(s)        