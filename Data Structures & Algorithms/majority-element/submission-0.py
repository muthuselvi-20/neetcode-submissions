class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fre = {}
        for i in nums:
            fre[i] = fre.get(i,0) + 1
        return max(fre,key = fre.get)    