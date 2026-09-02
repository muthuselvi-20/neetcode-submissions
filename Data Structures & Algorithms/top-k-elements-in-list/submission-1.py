class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        b = [[] for _ in range(len(nums)+1)]

        for num in nums:
            fre[num] = fre.get(num,0) + 1

        for num,val in fre.items():
            b[val].append(num)

        res=[]
        for i in range(len(b)-1,-1,-1):
            for num in b[i]:
                res.append(num)
                if len(res) == k:
                    return res